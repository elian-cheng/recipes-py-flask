from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_migrate import Migrate

app = Flask(__name__)

# You can use 3 slashes /// - means to a relative path (from root dir) or 4 slashes //// is an absolute path.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50))
    date_posted = db.Column(
        db.DateTime, nullable=False, default=datetime.now(timezone.utc)
    )

    def __repr__(self):
        return "Recipe" + str(self.id)


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


all_recipes = [
    {
        "title": "Recipe 1",
        "description": "Some ingredients for 1 recipe",
        "author": "Joey",
    },
    {"title": "Recipe 2", "description": "Some ingredients for 2 recipe", "author": ""},
]


@app.route("/recipes/")
def recipes():
    return render_template("recipes.html", recipes=all_recipes)


if __name__ == "__main__":
    app.run(debug=True)
