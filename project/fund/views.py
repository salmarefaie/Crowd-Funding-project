from django.shortcuts import render
from django.http import HttpResponse
from .models import fund

from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:login')
def fundpage(request):
    return render (request , 'fund/fundpage.html')

@login_required(login_url='authentication:login')
def confirmationpage(request):
    return render (request , 'fund/confirmationpage.html', {"fund":fund.objects.all().order_by('username')})