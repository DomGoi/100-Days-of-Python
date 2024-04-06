import datetime
import os
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegistrationForm, LoginForm, CommentForm
from flask_login import login_required
from typing import List


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
admin_mail=os.environ.get("MAIL_ADMIN")
year_now=datetime.datetime.now().year

ckeditor = CKEditor(app)
Bootstrap5(app)




# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    img_url = db.Column(db.String(250), nullable=False)
    comments=relationship("Comment", back_populates="parent_post")



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=True)
    posts = relationship("BlogPost", back_populates="author")
    comments= relationship("Comment", back_populates="author")


class Comment(UserMixin, db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    text = db.Column(Text)
    parent_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))

    author = relationship("User", back_populates="comments")
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()

login_manager=LoginManager()
login_manager.login_view='login'
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.email == admin_mail:
            return f(*args, **kwargs)
        else:
            return render_template("authorization.html", year=year_now)
    return wrapper

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




@app.route('/register', methods=["POST","GET"])
def register():
    form=RegistrationForm()

    if form.validate_on_submit():
        email=form.email.data
        result=User.query.filter_by(email=email).first()

        if result:
            flash("The email is already registered. Please Log in.")
            return redirect(url_for('login'))

        else:
            hashed_password=generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=10)

            new_user=User(
                name=form.name.data,
                email=form.email.data,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form, year=year_now)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["POST","GET"])
def login():
    form= LoginForm()
    admin=admin_mail
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data

        user=User.query.filter_by(email=email).first()
        if not user:
            flash("The email do not exist in our database. Try agin.", 'error')

        elif not check_password_hash(user.password, password):
            flash("Invalid password. Try again.", 'error')

        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=form, admin=admin, user=current_user, year=year_now)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, year=year_now)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["POST","GET"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    admin=admin_mail
    comments=db.get_or_404(Comment, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please log in to add comment.")
            return redirect(url_for('login'))

        new_comment=Comment(
            text=comment_form.comment_text.data,
            author_id=current_user,
            author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
        comment_form.comment_text.data = ""
        return redirect(url_for('show_post', post_id=post_id))

    return render_template("post.html", post=requested_post, admin=admin, user=current_user, year=year_now,
                           comment_form=comment_form, comments=comments)



@app.route("/new-post", methods=["GET", "POST"])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, year=year_now)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, year=year_now)





# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@login_required
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", year=year_now)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=year_now)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
