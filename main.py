from flask import Flask

app=Flask(__name__)


print(__name__)

@app.route("/")
def hello_world():
    return"<p><h1> Hellow World!</h1></p>"


@app.route("/ly")
def love():
    return"<p><h1>LOVE YOU !!!</h1></p>"



if __name__=="__main__":
    app.run()