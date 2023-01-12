from django.contrib import admin
from django.urls import path 
from .import views
from .models import project

urlpatterns = [
    path('',views.viewProjects, name="viewProjects")
]