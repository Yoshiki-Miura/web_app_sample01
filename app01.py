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


if __name__ == '__main__':
    app.run(debug=True)