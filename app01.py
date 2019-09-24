import numpy as np
from flask import Flask

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
    if r < 0.5:
        return "凶"
    elif 0.5 <= r and r < 0.8:
        return "吉"
    else:
        return "大吉"


if __name__ == '__main__':
    app.run(debug=True)