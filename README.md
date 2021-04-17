# CookingAppBackend
Simple DRF project which provides CRUD functionality for a basic cooking application.

You have to be authenticated in order to be able to create a new recipe.
Only the creator of the recipe can update/delete it.

## Rest Api Endpoints:
GET /api/recipes - provides list of all recipes

GET /api/recipes/:id - provides information for a specific recipe

POST /api/recipes/create - creates a new recipe

PUT /api/recipes/edit/:id - edits a recipe

DELETE /api/recipes/delete/:id - deletes a recipe

## The application is hosted on the following link: https://cooking-app-backend-vasil-loz.herokuapp.com/api/recipes/
