from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor=CKEditor(app)

class BlogForm(FlaskForm):
    title=StringField("Title", validators=[DataRequired()])
    subtitle=StringField("Subtitle", validators=[DataRequired()])
    author_name=StringField("Author name", validators=[DataRequired()])
    img_url=StringField("Image url", validators=[DataRequired(), URL()])
    blog_body=CKEditorField("Body", validators=[DataRequired()])
    submit=SubmitField("Submit")

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        column_names=self.__table__.columns.keys()
        return {column: getattr(self,column) for column in column_names}


with app.app_context():
    db.create_all()





@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    all_posts=BlogPost.query.all()
    posts = [p.to_dict() for p in all_posts]

    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post =db.session.execute(db.select(BlogPost).filter(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def new_post():

    form = BlogForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.blog_body.data,
            img_url=form.img_url.data,
            author=form.author_name.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def editing_post(post_id):
    post_to_edit=BlogPost.query.get(post_id)
    form=BlogForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        author_name=post_to_edit.author,
        img_url=post_to_edit.img_url,
        blog_body=post_to_edit.body
    )

    if form.validate_on_submit():
        post_to_edit.title=form.title.data
        post_to_edit.subtitle=form.subtitle.data
        post_to_edit.author=form.author_name.data
        post_to_edit.img_url=form.img_url.data
        post_to_edit.body=form.blog_body.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, editing=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=["GET"])
def delete_post(post_id):
    post=BlogPost.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))



# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
