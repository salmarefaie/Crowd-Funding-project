from django.urls import path
from . import views

urlpatterns = [
    path('fundpage/' , views.fundpage , name="fundpage"),
    
]