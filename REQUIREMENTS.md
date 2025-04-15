CMPE 131 - Term Project - Recipe Book

Requirements Page:
#1: User Login
#2: User Logout
#3: Create Recipe
#4: Edit Recipe
#5: Delete Recipe
#6: View Recipe
	Name: View Recipe
	Summary: A user can view any recipe in the DB by clicking on the recipe.
	Actors: user
	Pre-condition(s): User must know name of the recipe to find and view. Login not required
	Trigger: User clicks on recipe from Recipes page
	Primary Sequence:
		1.) The user locates recipe from the Recipes page Recipes list
		2.) User clicks on recipe to view recipe data
		3.) System takes user to recipe page to view all recipe information
		4.) System displays recipe information followed by comments and ratings
	Alternate Sequence:
		1.) User cannot locate recipe on Recipes page
		2.) User has the option to look for recipe through search bar
#7: Search Recipe
	Name: Search Recipe
	Summary: A user can search for any recipe that exists in the DB.
	Actors: user
	Pre-conditions: User must know name or recipe or type.
	Trigger: User clicks on search bar to enter recipe name.
	Primary Sequence:
		1.) The user clicks on the search bar and begins search.
		2.) After each letter is entered, the system pulls up a dropdown of all possible recipes
		3.) The user can also filter the search by type
#8: Rate Recipe
#9: Comment on Recipe
#10: View User Profile
