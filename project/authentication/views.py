from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm , CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    context = {"form":form}
    
    if request.method == 'POST': # if request.method equal to post # then let's through the data to the form
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'Auth/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'Auth/login.html')
def index(request):
    context = {}
    return render(request, 'index.html')