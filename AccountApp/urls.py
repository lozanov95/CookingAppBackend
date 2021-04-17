from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken

app_name = 'recipes'

urlpatterns = [
    path('login/', CustomAuthToken.as_view())
]
