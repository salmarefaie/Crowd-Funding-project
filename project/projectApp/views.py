from django.shortcuts import render,redirect
from .forms import project_form
from .models import project
from django.contrib.auth.decorators import login_required

# Create your views here.

# show all projects
def viewProjects(request):
    return render(request, 'projectApp/projects.html', {"projects":project.objects.all()})

# show single project
def viewSingleProject (request,id):
    singleProject= project.objects.get(pk = id)
    return render(request,'projectApp/singleProject.html',{"project":singleProject})

# delete project
@login_required(login_url='authentication:login')
def deleteProject  (request,id):
    deleteProject= project.objects.get(pk = id)
    deleteProject.delete()
    projects = project.objects.all().order_by('id')
    return render(request,'projectApp/projects.html',{"projects":projects})

# create project
@login_required(login_url='authentication:login')
def createProject(request):
    project = project_form(request.POST, request.FILES)
    if project.is_valid():
        userID = project.save(commit=False) 
        userID.user = request.user
        userID.save()
        project.save()
    else :
        print("not valid")
    return render(request,'projectApp/createProject.html',{"form":project_form})

# edit project
@login_required(login_url='authentication:login')
def editProject (request,id):
    project_id= project.objects.get(pk = id)
    form = project_form(request.POST or None,instance=project_id)
    if form.is_valid():
        form.save()
        return redirect('viewProjects')
    else :
        print("not valid")
    return render(request,'projectApp/editProject.html',{"project" : project_id,"form":form}) 

# show user projects
def userProjects (request):
    project= project.objects.filter(user=request.user.id).values()
    return render(request,'pages/showUserProjects.html',{"projects": project})