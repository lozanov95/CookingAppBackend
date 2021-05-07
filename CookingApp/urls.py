from django.urls import path
from .views import api_create_recipe_view, api_detail_recipe_view, api_update_recipe_view, api_delete_recipe_view, \
    RecipeGetApi, api_get_comment_view, api_create_comment_view

app_name = 'recipes'

urlpatterns = [
    # Recipes
    path('', RecipeGetApi.as_view()),
    path('/', RecipeGetApi.as_view()),
    path('/<int:pk>', api_detail_recipe_view),
    path('/create', api_create_recipe_view),
    path('/delete/<int:pk>', api_delete_recipe_view),
    path('/edit/<int:pk>', api_update_recipe_view),

    # Comments

    path('/<int:recipe_id>/comments', api_get_comment_view),
    path('/<int:recipe_id>/comments/create', api_create_comment_view)
]
