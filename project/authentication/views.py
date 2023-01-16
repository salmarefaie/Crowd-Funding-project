from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.



def registerPage(request):
    form = UserCreationForm()
    context = {"form":form}
    
    if request.method == 'POST': # if request.method equal to post 
                                # then let's through the data to the form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html')
def index(request):
    context = {}
    return render(request, 'index.html')