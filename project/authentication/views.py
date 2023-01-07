from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def registerPage(request):
    form = UserChangeForm()
    
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {"form":form}
    return render(request, 'register.html',context)

def loginPage(request):
    context = {}
    return render(request, 'login.html',context)
