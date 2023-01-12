from django.shortcuts import render
from .models import project

# Create your views here.
def viewProjects(request):
    return render(request, 'projectApp/projects.html', {"projects":project.objects.all()})