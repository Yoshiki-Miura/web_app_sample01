import numpy as np
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>Hello, world from Japan</h1>"


@app.route("/goodbye")
def goodbye():
    return "goodbye"


@app.route("/add/<a>/<b>")
def add(a, b):
    return str(int(a) + int(b))


@app.route("/omikuji")
def omikuji():
    r = np.random.random()
    if r < 0.4:
        result = "大凶"
    elif r < 0.7:
        result = "凶"
    elif r < 0.9:
        result = "吉"
    else:
        result = "大吉"

    return render_template("omikuji.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
