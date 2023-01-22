from django.contrib import admin
from django.urls import path 
from .import views
from .models import project

urlpatterns = [
    path('',views.viewProjects, name="viewProjects"),
    path('singleProject/<id>',views.viewSingleProject, name="viewSingleProject"),
    path('deleteProject/<id>',views.deleteProject, name="deleteProject"),
    path('createProject',views.createProject, name="createProject"),
    path('editProject/<id>',views.editProject, name="editProject")
]