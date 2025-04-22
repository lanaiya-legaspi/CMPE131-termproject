from flask import Flask, render_template
from app import myapp_obj

@myapp_obj.route("/")
@myapp_obj.route("/home")
def main():
	return render_template("index.html")

@myapp_obj.route("/recipes")
def recipes():
	return render_template("recipes.html")

@myapp_obj.route("/recipe")
def recipeX():
	return render_template("recipe.html")

@myapp_obj.route("/grocery-list")
def grocery_list():
	return render_template("grocery-list.html")
