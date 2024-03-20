from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_babel import _, Babel
from flask_bootstrap import Bootstrap4
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

bootstrap=Bootstrap4(app)

def contain_at_sym(form, field):
    if "@" not in field.data:
        raise ValidationError(_("Name must contain @"))
    elif "." not in field.data:
        raise ValidationError(_("Name must contain ."))
class MyForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=8, message=_('Little short for an email address?')),
        Email(message=_('That\'s not a valid email address.')), contain_at_sym
    ])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=8, max=30),
    ])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        if form.name.data=="admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
