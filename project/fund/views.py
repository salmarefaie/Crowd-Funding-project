from django.shortcuts import render
from django.http import HttpResponse


def fundpage(request):
    return render (request , 'fund/fundpage.html')

def confirmationpage(request):
    return render (request , 'fund/confirmationpage.html')