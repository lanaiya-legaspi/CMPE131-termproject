#imports
from flask import Flask, render_template
from datetime import datetime
from app import myapp_obj, db
from app.models import Recipe, Recipe_Ingredient
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
@myapp_obj.route("/recipe-<id>")
def recipeX(id):
	recipe = db.session.get(Recipe, id)
	ing_descs = get_Ing_Descs(id)
	recipe_qtys = Recipe_Ingredient.query.filter(Recipe_Ingredient.recipe_id==id).all()
	recipe_insns = ['step1', 'step2', 'step3'] # insns to be parsed soon
	rform = RatingsForm()
	cform = CommentsForm()
	if cform.validate_on_submit(): # comments form validation / db submission
		cmt_tmstp = str(datetime.now())
		comment = Recipe_Comment(
			comment_desc=form.comment_desc.data,
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
		return redirect("/")
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
	
