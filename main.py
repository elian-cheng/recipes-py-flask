from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/home/")
def home():
    return render_template("index.html")


# http://127.0.0.1:5000/home/Joey
# Dynamic route
@app.route("/home/<string:name>/")
def helloName(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
