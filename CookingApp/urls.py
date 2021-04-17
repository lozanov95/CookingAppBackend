from django.urls import path
from .views import api_create_recipe_view, api_detail_recipe_view, api_update_recipe_view, api_delete_recipe_view, \
    RecipeGetApi

app_name = 'recipes'

urlpatterns = [
    path('', RecipeGetApi.as_view()),
    path('<int:pk>', api_detail_recipe_view),
    path('create', api_create_recipe_view),
    path('delete/<int:pk>', api_delete_recipe_view),
    path('edit/<int:pk>', api_update_recipe_view),
]
