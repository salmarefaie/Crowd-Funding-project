from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm , CreateUserForm
from django.contrib.auth import authenticate ,login , logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def registerPage(request):
    form = CreateUserForm()
    context = {"form":form}
    
    if request.method == 'POST': # if request.method equal to post # then let's through the data to the form
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for " + user)
            return redirect('authentication:login')
        
        
    return render(request, 'Auth/register.html', context)

def loginPage(request):
    context = {}
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username, password=password )
        if user is not None:
            login(request,user)
            return redirect('authentication:home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'Auth/login.html')

    return render(request, 'Auth/login.html')
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    
    return redirect('authentication:login')


# @login_required(login_url='authentication:login')
def index(request):
    context = {}
   
    return render(request, 'index.html')