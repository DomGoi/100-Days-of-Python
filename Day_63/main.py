from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
boot = Bootstrap4(app)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project_movie.db"
db.init_app(app)

class Movie(db.Model):
  id:Mapped[int]=mapped_column(Integer,primary_key=True)
  title:Mapped[str]=mapped_column(String(250),unique=True)
  director:Mapped[str]=mapped_column(String(250),nullable=False)
  rating:Mapped[float]=mapped_column(Float,nullable=False)

with app.app_context():
  db.create_all()


@app.route('/')
def home():
    all_movies=Movie.query.order_by(Movie.title).all()

    return render_template('index.html', all_movies=all_movies)

@app.route("/edit/<int:id>", methods=["POST","GET"])
def edit(id):
    movie=Movie.query.get_or_404(id)
    if request.method=="POST":
        movie.rating=request.form.get("rating")
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie)




@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_movie=Movie(
                title = request.form.get("title"),
                director = request.form.get("director"),
                rating = request.form.get("rating")
                    )
            db.session.add(new_movie)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True, port=5100)
