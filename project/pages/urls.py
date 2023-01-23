from django.urls import path
from . import views
urlpatterns = [

    path('register', views.viewRegister, name="Register"),
    path('login', views.viewLogin, name="Login"),
]