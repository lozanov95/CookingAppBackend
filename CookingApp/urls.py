from django.urls import path
from .api import RecipeCreateApi, RecipeGetApi, RecipeDeleteApi, RecipeEditApi, RecipeGetByIdApi

urlpatterns = [
    path('', RecipeGetApi.as_view()),
    path('<int:pk>', RecipeGetByIdApi.as_view()),
    path('create', RecipeCreateApi.as_view()),
    path('delete/<int:pk>', RecipeDeleteApi.as_view()),
    path('edit/<int:pk>', RecipeEditApi.as_view()),
]
