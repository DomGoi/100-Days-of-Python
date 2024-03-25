from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///top_10_movies.db"
db.init_app(app)

class Movie_table(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

URL = "https://api.themoviedb.org/3/search/movie?include_adult=true&language=en-US&page=1"
API_KEY="c1d619a834f6e17eb4c97cc3a5aa4751"


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie_table).order_by(Movie_table.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["POST","GET"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        query=request.form.get("title")

        headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMWQ2MTlhODM0ZjZlMTdlYjRjOTdjYzNhNWFhNDc1MSIsInN1YiI6IjY2MDA2ZWFlN2Y2YzhkMDE2MzZmNTQ1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gYXBfFLcBgkm7gQ8bqaJL_DFUhJhfh1CGJQSarKzsps"
        }

        parameters={
                "query":query,
                "adult":"True"

        }

        response = requests.get(URL, headers=headers, params=parameters)
        response.raise_for_status()

        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)



@app.route("/delete")
def delete():
    movie_id=request.args.get("id")
    movie = db.get_or_404(Movie_table, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

with app.app_context():
    db.create_all()



@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie_table, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:

        url = f"https://api.themoviedb.org/3/movie/{movie_api_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMWQ2MTlhODM0ZjZlMTdlYjRjOTdjYzNhNWFhNDc1MSIsInN1YiI6IjY2MDA2ZWFlN2Y2YzhkMDE2MzZmNTQ1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.gYXBfFLcBgkm7gQ8bqaJL_DFUhJhfh1CGJQSarKzsps"
        }

        response_find = requests.get(url, headers=headers)
        response_find.raise_for_status()

        data=response_find.json()
        new_movie=Movie_table(
        title=data["title"],
        year = data["release_date"].split("-")[0],
        img_url=f"{'https://image.tmdb.org/t/p/w500'}{data['poster_path']}",
        description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)
