from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.registerPage),
    path('login/', views.loginPage)
    ]
# 