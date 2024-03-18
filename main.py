from flask import Flask, redirect, render_template, request
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
@app.route("/home/")
def home():
    num_recipes = Recipe.query.count()
    return render_template("index.html", num_recipes=num_recipes)


# http://127.0.0.1:5000/home/Joey
# Dynamic route
@app.route("/home/<string:name>/")
def helloName(name):
    return f"Hello, {name}!"


@app.route("/recipes/", methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        recipe_title = request.form["title"]
        recipe_description = request.form["description"]
        new_recipe = Recipe(
            title=recipe_title, description=recipe_description, author="Elian"
        )
        db.session.add(new_recipe)
        db.session.commit()
        return redirect("/recipes/")
    else:
        all_recipes = Recipe.query.order_by(Recipe.date_posted).all()
        return render_template("recipes.html", recipes=all_recipes)


@app.route("/recipes/delete/<int:id>/")
def delete(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect("/recipes/")


@app.route("/recipes/edit/<int:id>/", methods=["GET", "POST"])
def edit(id):
    recipe = Recipe.query.get_or_404(id)
    # copy and past the post query.
    if request.method == "POST":
        recipe.title = request.form["title"]
        recipe.description = request.form["description"]
        recipe.category = request.form["category"]
        db.session.commit()
        return redirect("/recipes/")
    else:
        return render_template("edit.html", recipe=recipe)


@app.route("/recipes/new/", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        recipe_title = request.form["title"]
        recipe_description = request.form["description"]
        new_recipe = Recipe(
            title=recipe_title, description=recipe_description, author="Elian"
        )
        db.session.add(new_recipe)
        db.session.commit()
        return redirect("/recipes/")
    else:
        return render_template("new_recipe.html")


if __name__ == "__main__":
    app.run(debug=True)
