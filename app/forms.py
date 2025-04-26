#imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, HiddenField

#class to validate anad handle recipe information
class RecipeForm(FlaskForm):
	recipe_id = HiddenField()
	recipe_desc = StringField('RECIPE DESCRIPTION', [validators.DataRequired()])
	recipe_type = StringField('Recipe Type', [validators.DataRequired()])
#	recipe_servings = IntegerField('Recipe Servings', [validators.DataRequired()])
#	recipe_rating = IntegerField('Recipe Rating', [validators.Length(min=1, max=1)])
	recipe_insns = StringField('RECIPE INSTRUCTIONS', [validators.DataRequired()])

#class to handle the comments form section
class CommentsForm(FlaskForm):
	comment_id = HiddenField()
	comment_desc = StringField('COMMENT', [validators.DataRequired()])
	submit = SubmitField('Comment')

#class to handle the ratings form section
class RatingsForm(FlaskForm):
	rating_id = HiddenField()
