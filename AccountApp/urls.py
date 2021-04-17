from django.urls import path
from .views import CustomAuthToken, RegisterView, api_logout

app_name = 'recipes'

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', api_logout),
]
