from django.shortcuts import render
from django.http import HttpResponse
from .models import fund
from .forms import fund_form

from django.contrib.auth.decorators import login_required



@login_required(login_url='authentication:login')
def confirmationpage(request):
    return render (request , 'fund/confirmationpage.html', {"fund":fund.objects.all().order_by('username')})

def createProject(request):
    fund = fund_form(request.POST, request.FILES)
    if fund.is_valid():
        userID = fund.save(commit=False) 
        userID.user = request.user
        userID.save()
        fund.save()
    else :
        print("not valid")
    return render(request,'fund/entrypage.html',{"form":fund_form})