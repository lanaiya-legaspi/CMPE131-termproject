#from app import db

#class User(db.Model):
#	__tablename__ = 'users'
#	user_id = db.Column(db.Integer, primary_key=True)
#	###
#	###

#class Recipe(db.Model):
#	__tablename__ = 'recipes'
#	recipe_id = db.Column(db.Integer, primary_key=True)
#	recipe_desc = db.Column(db.Column(db.String(100)))
#	recipe_type = db.Column(db.Column(db.String(50)))
#	recipe_servings = db.Column(db.Integer)
#	recipe_rating = db.Column(db.Integer)
#	recipe_insns = db.Column(db.Column(db.String(1000)))

#class Ingredient(db.Model):
#	__tablename__ = 'ingredients'
#	ing_id = db.Column(db.Integer, primary_key=True)
#	ing_desc = db.Column(db.String(200))
#	ing_type = db.Column(db.String(30))

#class Recipe_Ingredients(db.Model):
#	__tablename__ = 'recipe_ingredients'
#	recipe_id = db.Column(db.Integer, foreign_key=True)
#	ing_id = db.Column(db.Integer, foreign_key=True)
#	ing_qty = db.Column(db.Double)
#	ing_uom = db.Column(db.String(10))

#class Recipe_Comments(db.Model):
#	__tablename__ = 'recipe_comments'
#	comment_id = db.Column(db.Integer, primary_key=True)
#	comment_desc = db.Column(db.String)
#	user_id = db.Column(db.Integer, foreign_key=True)
#	recipe_id = db.Column(db.Integer, foreign_key=True)
#	comment_tmstp = db.Column(db.DateTime)

#class Recipe_Ratings(db.Model):
#	__tablename__ = 'recipe_ratings'
#	rating_id = db.Column(db.Integer, primary_key=True)
#	user_id = db.Column(db.Integer, foreign_key=True)
#	recipe_id = db.Column(db.Integer, foreign_key=True)
#	recipe_rating = db.Column(db.Integer)
