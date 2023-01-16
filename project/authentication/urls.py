from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.registerPage,name='register'),
    path('login/', views.loginPage,name='login')
    
    ]
app_name = 'authentication'
