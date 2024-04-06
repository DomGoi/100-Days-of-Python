import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

#Registration Form
class RegistrationForm(FlaskForm):
    name = StringField("Input your name", validators=[DataRequired()])
    email = StringField("Input e-mail address", validators=[DataRequired(), Email()])
    password = PasswordField("Input your password", validators=[DataRequired()])
    submit = SubmitField("Register Me")

#Login Form

class LoginForm(FlaskForm):
    email=StringField("E-mail address", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    submit=SubmitField("Log In")

#Comment Form
class CommentForm(FlaskForm):
    comment_text=CKEditorField("Comment", validators=[DataRequired()])
    date_posted=datetime.datetime.today().strftime("%B %d, %Y")
    submit=SubmitField("Post")
