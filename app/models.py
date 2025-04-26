from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

class Recipe(db.Model):
	__tablename__ = 'recipes'
	recipe_id = db.Column(db.Integer, primary_key=True)
	recipe_desc = db.Column(db.String(100))
	recipe_type = db.Column(db.String(50))
	recipe_servings = db.Column(db.Integer)
	recipe_rating = db.Column(db.Integer)
	recipe_insns = db.Column(db.String(1000))

	def __repr__(self):
		return f'<Recipe: {self.recipe_desc}>'

class Ingredient(db.Model):
	__tablename__ = 'ingredients'
	ing_id = db.Column(db.Integer, primary_key=True)
	ing_desc = db.Column(db.String(200))
	ing_type = db.Column(db.String(30))

class Recipe_Ingredient(db.Model):
	__tablename__ = 'recipe_ingredients'
	recing_id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
	ing_id = db.Column(db.Integer, db.ForeignKey('ingredients.ing_id'))
	ing_qty = db.Column(db.Double)
	ing_uom = db.Column(db.String(10))

class Recipe_Comment(db.Model):
	__tablename__ = 'recipe_comments'
	comment_id = db.Column(db.Integer, primary_key=True)
	comment_desc = db.Column(db.String)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
	comment_tmstp = db.Column(db.DateTime)

class Recipe_Rating(db.Model):
	__tablename__ = 'recipe_ratings'
	rating_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
	recipe_rating = db.Column(db.Integer)
