from django.urls import path
from .views import CustomAuthToken, RegisterView

app_name = 'recipes'

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
