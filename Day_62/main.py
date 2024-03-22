from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired, ValidationError
from flask_babel import _, Babel
import csv

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
babel = Babel(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)


def custom_sym(form, field):
    if "." not in field.data:
        raise ValidationError(_("URL must contain ."))
    elif "http" or "https" not in field.data:
        raise ValidationError(_("URL must contain http or https protocol."))
    elif "www" not in field.data:
        raise ValidationError(_("URL must contain www."))

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location=URLField('Cafe location', validators=[
        DataRequired(),
    ])
    open_time=TimeField('Opening Time', )
    close_time=TimeField('Closing Time',)
    coffee = SelectField(u'Coffee',
                         choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                  ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')], validators=[
            DataRequired()
        ])
    wifi=SelectField(u'Wifi', choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[
        DataRequired()
    ])
    power=SelectField(u'Power', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], validators=[
        DataRequired()
    ])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        print("True")
        cafe=form.cafe.data
        location=form.location.data
        open_time=form.open_time.data
        close_time=form.close_time.data
        coffee=form.coffee.data
        wifi=form.wifi.data
        power=form.power.data

        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer=csv.writer(csv_file)
            csv_writer.writerow([cafe,location,open_time,close_time,coffee,wifi,power])

        return redirect('cafes')

    return render_template('add.html', form=form)


@app.route('/cafes', methods=["POST", "GET"])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
