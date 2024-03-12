from flask import Flask, render_template
import random

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


random_num=random.randint(0,9)
print(random_num)
@app.route("/<number>")
def check_number(number):
    if int(number)>9:
        return render_template('wrong.html')
    if int(number) > random_num:
        return render_template('too_high.html')
    elif int(number)<random_num:
        return render_template('too_low.html')
    elif int(number) == random_num:
        return render_template('equal.html')


if __name__ == "__main__":
    app.run(debug=True)
