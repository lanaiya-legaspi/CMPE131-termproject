## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. User Registration - A visitor can create an account by providing a email and password.
2. User Login - Registered users can log in using their email and password.
3. User Log out - Logged-in users can log out of their account securely.
4. Create Recipe - Logged-in users can add new recipes with title, description, ingredients, and instructions
5. Edit Recipe - Users can update their own recipes after creation
6. View Recipe - A user can view any recipe on the cite by clicking the recipe name.
7. Search Recipe - A user can search for any recipe that exists on the cite.
8. Rate Recipe - A user can give each recipe a rating which will be added to an overall average rating for each recipe.
9. Comment on Recipe - A user can add a comment and view comments in the Comments section under the recipe information.
10. View User Profile - A user can view their profile with their account information including ratings and comments.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
2. non-functional

## Use Case #1 (Gerardo)
- **User Registration**
- **Pre-condition:** User must not be currently registered in the system
- **Trigger:** Visitor clicks the "Sign up" button
- **Primary Sequence:**
1. Visitor visits the website
2. Visitor clicks "sign up" button
3. System displays registration form
4. Visitor enters name, email, and password
5. System confirms the inputed data
6. System stores the users information in the database
7. System redirects user to login page
- **Primary Postconditions:** A new user account is created and stored
- **Alternate Sequence:**
1. User enters invalid email or password
2. System displays error message and prevents registration

## Use Case #2 (Gerardo)
- **User Login**
- **Pre-condition:** User has previously registered
- **Trigger:** User clicks the “Login” button and enters email and password
- **Primary Sequence:**
1. User clicks on "login" button
2. System displays login form
3. User enters email and password
4. System validates the credentials
5. System logs in the user and redirects them to homepage
- **Primary Postconditions:** User is confirmed and granted access to their account
- **Alternate Sequence**
1. User enters incorrect email or password
2. System prompts an error and asks for re-entry

## Use Case #3 (Gerardo)
- **User Logout**
- **Pre-condition:** User must be logged into their account
- **Trigger:** User clicks on "Logout" button
- **Primary sequence:**
1. User clicks on the “Logout” option
2. System clears/ends users session
3. System redireects user to home/login page
- **Primary Postcondition:** User is securely logged out
- **Alternate Sequence:**
1. User clicks “Logout” but has multiple tabs of the site open
2. System logs out user from the current tab
3. When the user interacts with another open tab, the system detects it and redirects them to the login page

## Use Case #4 (Gerardo)
- **Create Recipe**
- **Pre-condition:** User must be logged in
- **Trigger:** User clicks the “Create Recipe” or the "+" button
- **Primary sequence:** 
1. User clicks "create Recipe"
2. System displays the recipe fill out form
3. User fills in recipe name, description, ingredients, and instructions
4. User confirms recipe and clicks "done"
5. System validates and saves the recipe to the database
6. System redirects user to the new recipe’s page
- **Primary Postcondition:** New recipe is stored and published
- **Alternate Sequence:**
1. User submits incomplete form
2. System highlights missing section and prevents publication

## Use Case #5 (Gerardo)
- **Edit Recipe**
- **Pre-condition:** User is logged in and is the owner of the recipe they wish to edit
- **Trigger:** User clicks “Edit” on their recipe page
- **Primary sequence:**
1. User clicks "My Recipes" tab 
2. User clicks on recipe they want to edit
3. User clicks the "edit" button
4. System displays editable fill out form
5. User modifies recipe and confirms changes
6. System validates and saves the changes to the database
7. System displays the updated recipe
- **Primary Postcondition:** The recipe is updated with the new information inputed
- **Alternate Sequence:**
1. User attempts to edit a recipe that does not belong to them
2. System denies access and shows an error message


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
- Comment on Recipe
- **Pre-condition:** User is logged in and on a specific recipe page.
- **Trigger:** User clicks the "Add comment" button.
- **Primary Sequence:** 
1. User clicks on a recipe to go to the specific recipe page.
2. User scrolls down to the Comments section.
3. User enters their comment in the text box provided.
4. User clicks the "Add comment" button.
5. System checks the word count to verify it is less than 250 words.
6. System grabs the timestamp and username.
7. System adds the comment with username and timestamp below the recipe section.
- **Primary Postcondition:** User's comment is added to recipe page.
- **Alternate Sequence**
1. 

## Use Case #10 (Lanaiya)
- View User Profile
