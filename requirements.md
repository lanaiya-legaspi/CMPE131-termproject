## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. requirement <should be 1 sentence that describes requirement>
2. requirement
3. requirement
4. requirement
5. requirement
6. View Recipe - A user can view any recipe on the cite by clicking the recipe name.
7. Search Recipe - A user can search for any recipe that exists on the cite.
8. Rate Recipe - A user can give each recipe a rating which will be added to an overall average rating for each recipe.
9. Comment on Recipe - A user can add a comment and view comments in the Comments section under the recipe information.
10. View User Profile - A user can view their profile with their account information including ratings and comments.
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
2. non-functional

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>

1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...

## Use Case #6 (Lanaiya)
- **View Recipe**
- **Pre-condition:** User must know name of the recipe to find and view.
- **Trigger:** User clicks on recipe from Recipes page
- **Primary Sequence:**
1. The user locates recipe from the Recipes page Recipes list
2. User clicks on recipe to view recipe information
3. System takes user to recipe page
4. System displays all recipe information on screen
5. System displays comments/rating
- **Primary Postconditions:** User views recipe on their screen.
- **Alternate Sequence**
1. User cannot locate recipe on Recipes page
2. User has the option to look for recipe through search bar or filter by recipe type.


## Use Case #7 (Lanaiya)
- **Search Recipe**
- **Pre-condition:** User must know title of recipe or ingredient keywords.
- **Trigger:** User clicks on search bar and starts typing.
- **Primary Sequence**
1. The user goes to the Recipes page and locates the search bar towards the top.
2. The user clicks the button to do a search by title or ingredient.
3. The user clicks the search bar to type.
4. For each letter entered, the system looks for a related recipe based on search criteria
5. The system locates the recipe and displays the title in the dropdown as a clickable link.
6. The user clicks the desired recipe title.
7. The system takes user to the recipe page that was chosen
- **Primary Postcondition:** User views recipe on their screen.
- **Alternate Sequence**
1. User does not know the title or recipe ingredients.
2. The user can view a list of recipes under search bar organized by type (Appetizer, Entree, Dessert, Drink)
3. The user can locate the recipe or a similar one that is available on the website
- **Alternate Sequence**
1. The desired recipe does not pop up on the dropdown.
2. The user has an option to view recipes of a similar type.
3. The user also has an option to create/add a new recipe.

## Use Case #8 (Lanaiya)
- **Rate Recipe**
- **Pre-conditions:** User must be logged in and know the recipe they would like to rate.
- **Trigger:** User clicks on the stars to choose a rating from 1-5.
- **Primary Sequence**
1. The user chooses and views a specific recipe.
2. To the right of the recipe name, the system will display 5 stars.
3. The user clicks one of the stars to choose a rating.
4. The system adds the rating to the ratings table.
5. The system calculates the new average rating for the recipe.
6. The system displays the new average to the right of the stars.
7. The system shows the total ratings under the stars.
- **Primary Postcondition:** User's rating is added to system and overall recipe rating
- **Alternate Sequence**
1. The user clicks the wrong star by accident.
2. The user clicks "Edit Rating" to change their rating.
3. The system recalculates and displays new rating.
- **Alternate Sequence**
1. The user clicks rating by accident, unintentionally.
2. The user can click "Remove Rating".
3. The system removes the rating from the table and recalculates
4. The system displays original rating from before accidental rating.

## Use Case #9 (Lanaiya)
- **Comment on Recipe**
- **Pre-condition:** User is logged in and on a specific recipe page.
- **Trigger:** User clicks the "Add comment" button.
- **Primary Sequence:** 
1. User clicks on a recipe to go to the specific recipe page.
2. User scrolls down to the Comments section.
3. User enters their comment in the text box provided.
4. User clicks the "Add comment" button.
5. System checks the word count to verify it is less than 1000 characters.
6. System grabs the timestamp and username.
7. System adds the comment with username and timestamp below the recipe section.
- **Primary Postcondition:** User's comment is added to recipe page.
- **Alternate Sequence**
1. User enters more than 1000 characters and clicks enter.
2. An error line appears saying "Maximum number of characters reached."
3. System places tick in document to allow user to automatically reduce character count.


## Use Case #10 (Lanaiya)
