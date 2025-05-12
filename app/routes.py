#imports
from flask import Flask, render_template
from datetime import datetime
from app import myapp_obj, db
from app.models import Recipe, Recipe_Ingredient, Recipe_Rating, Recipe_Comment, Ingredient
from app.forms import RatingsForm, CommentsForm

# home page / recipe search page
@myapp_obj.route("/")
@myapp_obj.route("/home")
def main():
	recipes = Recipe.query.all() # pull all recipes from db
	return render_template("index.html", recipes=recipes)

# recipes page
@myapp_obj.route("/recipes")
def recipes():
	return render_template("recipes.html")

# recipe page
@myapp_obj.route("/recipe-<id>", methods=['GET', 'POST'])
def recipeX(id):
	recipe = db.session.get(Recipe, id)
	ing_descs = get_Ing_Descs(id)
	recipe_qtys = Recipe_Ingredient.query.filter(Recipe_Ingredient.recipe_id==id).all()
	recipe_insns = ['step1', 'step2', 'step3'] # insns to be parsed soon
	recform = Recipe
	rform = RatingsForm()
	cform = CommentsForm()

	if cform.validate_on_submit(): # comments form validation / db submission
		cmt_tmstp = str(datetime.now())
		comment = Recipe_Comment(
            comment_desc=cform.comment_desc.data,
			user_id=1,
			recipe_id=id,
			comment_tmstp=cmt_tmstp
		)
		db.session.add(comment)
		db.session.commit()
		print(f'Comment has been added!')
		return redirect("/")
	else:
		print("Comments Form Error")
	if rform.validate_on_submit(): # ratings form validation / db submission
		recipe_rating = request.form["exampleRadios"]
		recform.recipe_rating = calculate_overall_rating()
		rating = Recipe_Rating(recipe_id=id, recipe_rating=recipe_rating)
		db.session.add(rating)
		db.session.commit()
		recipe.recipe_rating = calculate_overall_rating()
		db.session.commit()
		return redirect("/recipe", recipe=recipe)
	else:
		print("Ratings Form Error")
	return render_template(
		"recipe.html",
		recipe=recipe,
		ing_descs=ing_descs,
		qtys=recipe_qtys,
		recipe_insns=recipe_insns,
		cform=cform, rform=rform
	)

def calculate_overall_rating(id):
	rows = Recipe_Rating.query.filter(Recipe_Rating.recipe_id==id)
	return 5

# my grocery list page
@myapp_obj.route("/grocery-list")
def grocery_list():
	return render_template("grocery-list.html")

from flask import session
from app.models import User

@myapp_obj.route("/user")
def user_profile():
    user_email = session.get("user")
    user = User.query.filter_by(email=user_email).first()
    return render_template("user.html", user=user)


#For the login page

from app.models import User
from flask import request, redirect, url_for, session, render_template

@myapp_obj.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Look up user in the database
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            session["user"] = user.email
            return redirect(url_for("user_profile"))
        else:
            error = "Invalid email or password."

    return render_template("login.html", error=error)

#For the register page

from app.models import User
from app import db

@myapp_obj.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None

    if request.method == "POST":
        print("FORM DATA:", request.form)
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        dob = request.form["dob"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            error = "Account already exists."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                email=email,
                password=password
            )
            db.session.add(new_user)
            db.session.commit()
            success = "Account created! You can now log in."

    return render_template("register.html", error=error, success=success)


@myapp_obj.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))





# routing definitions
def get_Ing_Descs(id):
	ingredients = Recipe_Ingredient.query.all()
	descs = []
	recipe_ings = Recipe_Ingredient.query.filter(Recipe_Ingredient.recipe_id==id).all()
      
# Adding a Recipe
@myapp_obj.route("/add-recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        title = request.form["recipe_desc"]
        recipe_type = request.form["recipe_type"]
        servings = request.form["recipe_servings"]
        instructions_raw = request.form["recipe_instructions"]
        ingredients_raw = request.form["ingredients"]

        # Save recipe to database
        new_recipe = Recipe(
            recipe_desc=title,
            recipe_type=recipe_type,
            recipe_servings=servings,
            recipe_rating=0,  # default rating
            recipe_insns=instructions_raw
        )
        db.session.add(new_recipe)
        db.session.commit()

        # Add ingredients
        ingredients_lines = ingredients_raw.strip().split("\n")
        for line in ingredients_lines:
            parts = line.strip().split(" ", 2)
            if len(parts) == 3:
                qty, uom, name = parts
            elif len(parts) == 2:
                qty, name = parts
                uom = "unit"
            else:
                continue  # skip malformed line

            # Check if ingredient exists
            ingredient = Ingredient.query.filter_by(ing_desc=name).first()
            if not ingredient:
                ingredient = Ingredient(ing_desc=name, ing_type="")
                db.session.add(ingredient)
                db.session.commit()

            # Link recipe and ingredient
            ri = Recipe_Ingredient(
                recipe_id=new_recipe.recipe_id,
                ing_id=ingredient.ing_id,
                ing_qty=qty,
                ing_uom=uom
            )
            db.session.add(ri)

        db.session.commit()
        return redirect(url_for("main"))

    return render_template("add_recipe.html")

#ediiting a recipe
@myapp_obj.route("/edit-recipe/<int:id>", methods=["GET", "POST"])
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    if request.method == "POST":
        recipe.recipe_desc = request.form["recipe_desc"]
        recipe.recipe_type = request.form["recipe_type"]
        recipe.recipe_servings = request.form["recipe_servings"]
        recipe.recipe_insns = request.form["recipe_insns"]

        db.session.commit()
        return redirect(url_for("recipeX", id=recipe.recipe_id))

    return render_template("edit_recipe.html", recipe=recipe)



	
