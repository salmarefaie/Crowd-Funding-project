from django.shortcuts import render
from .models import user

# Create your views here.
def viewLogin(request):
     return render(request,'pages/login.html')

def viewRegister(request):
     return render(request,'pages/register.html')


