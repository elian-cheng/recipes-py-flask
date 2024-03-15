# We'll start by setting up everything in a Python environment, and then we'll seamlessly integrate it into our code. Let's enhance our database by adding a few entries to it. To do this, we'll need to import the models and continue our work in the Python environment. Type into your Terminal:

# python

# Or open Python Console. Let's practice with queries to the database.

from main import Recipe, db, app

# Next query will implement READ functionality:

Recipe.query.all()

# This command will get all the Recipes from the table. But we received an empty list because we haven't put anything in the database yet. So, we want to add a new model. It is CREATE functionality.


db.session.add(
    Recipe(title="Pizza 1", description="Description for pizza 1", author="Joey")
)

all_recipes = [
    {
        "title": "Recipe 1",
        "description": "Some ingredients for 1 recipe",
        "author": "Joey",
    },
    {"title": "Recipe 2", "description": "Some ingredients for 2 recipe", "author": ""},
]

# Now, let's repeat the previous command, Recipe.query.all(). And we have the first entry in our database. Repeat the second command and add Recipe 2. Let's do it through variables.

# pizza_2 = Recipe(title="Pizza 1", description="Description for pizza 1")

# db.session.add(pizza_2)

# Also, we can READ from the database in different ways.

# We can slice the list with our Recipes:

Recipe.query.all()[1]

# We will get a second Recipe.

# And we can receive a specific field:

Recipe.query.all()[1].title

Recipe.query.all()[1].description

# We can read only the first one, too. It just gets the first one from the entire list:

Recipe.query.first()

# Also, you can assign the result to some variable, and it will work accordingly:

all_recipes = Recipe.query.all()
all_recipes[0]
all_recipes[1]
# Let's check if we will go out of range.
all_recipes[5]
# We can't, as you can see.
# We can filter by things. We can actually call the .filter_by() method and specify what we are going to filter so far as we filter by title, we can filter by any model's attribute:

Recipe.query.filter_by(title="Pizza 1").all()

# So, you can see only Recipe 1 because it is related to our query condition.

# There is also a get method. What does it do? It gets whichever object by its id or other unique attribute:

Recipe.query.get(5)

# If we go out of range, nothing breaks. But if you print it out, it will return None. It's just an empty thing.

# However, you might encounter some warnings with this method. In such cases, it's better to use the following approach:

db.session.get(Recipe, 1)

# There is another get_or_404() method. We will use it a little bit later.

# There are pretty much things we will use in our application.

# And, lastly, very important different kinds of READ you can look at the official documentation if you want to know more.

# We made temporary entries to our database. To save our examples, we need to commit it by command:

db.session.commit()

# Now, the changes are happening in the DB file, and if we completely restart the entire computer, close all these, or have a different terminal session, this data will be preserved in the file even if we move this file to a different computer.

# Let's discuss the process of DELETING data from the database. Return to our Python Console and give the delete query a try. Deleting is a simple process – you just need to invoke the database object and use the delete() method instead of add(). Then, pass the object you want to delete.

# If you've closed your terminal or Python Console, don't worry. You can simply import db, Recipe, app to get back on track.
recipe = Recipe.query.get(4)
db.session.delete(recipe)
# we haven't commit this change yet.
db.session.commit()
# now it should work now and its gone.
Recipe.query.all()

# Let's talk about how to UPDATE elements, allowing you to edit specific parts of a recipe or update the entire recipe, completing the CRUD operations in Flask.

# Remember how we easily accessed different fields of our model by using the following method:
Recipe.query.get(1).author
# Just assign a new value to the attribute:
Recipe.query.get(1).author = "Monica"
db.session.commit()
# This command is just to check the functionality of the previous two:
Recipe.query.filter_by(author="Monica").all()

# Working outside of the context error solution
from main import app

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
app_ctx.pop()
