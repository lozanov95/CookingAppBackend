# CookingAppBackend
Simple DRF project which provides CRUD functionality for a basic cooking application.

You have to be authenticated in order to be able to create a new recipe.
Only the creator of the recipe can update/delete it.

## Rest Api Endpoints:

### Authentication endpoints
POST /api/token-auth/register/ - register new user if you provide valid username, password an email. This endpoint does not log you in

POST /api/token-auth/login/ - logs you in when you provide valid username and password. Returns Authentication token and user id

POST /api/token-auth/logout/ - Logs the current user out. 
 
### Cooking app endpoints 

#### Recipes
 
GET /api/recipes - provides list of all recipes

GET /api/recipes/:id - provides information for a specific recipe

GET /api/recipes?creator_id=:id - gets recipes from a specific creator

POST /api/recipes/create - creates a new recipe

PUT /api/recipes/edit/:id - edits a recipe

DELETE /api/recipes/delete/:id - deletes a recipe

##### Comments

GET /api/recipes/:id/comments - gets the comments of a specific recipe

POST /api/recipes/:id/comments/create - adds a comment for the specific recipe (requires authenticated user)

### The application is hosted on the following link: https://cooking-app-backend-vasil-loz.herokuapp.com/api/recipes/
### There is a frontend application that uses this api - https://cooking-app-frontend-vasil-loz.herokuapp.com/ - repo https://github.com/lozanov95/CookingAppFrontendReactJS
