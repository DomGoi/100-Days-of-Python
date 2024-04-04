import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecrestBlackMAssiveHoLe420'
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        input_email=request.form.get("email")

        res=User.query.filter_by(email == input_email).first()

        if res:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        else:
            hased_password=generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password= hased_password
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template("register.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')


        results=db.session.execute(db.select(User).where(User.email==email))
        user = results.scalar()
        if not user:
            flash("Email does not found in our database", 'error')

        elif not check_password_hash(user.password, password):
            flash("Invalid password. Please try again.", 'error')
            return redirect(url_for('login'))

        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")



@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", user_name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')



if __name__ == "__main__":
    app.run(debug=True)
