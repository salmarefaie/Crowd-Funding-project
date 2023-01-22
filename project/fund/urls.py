from django.urls import path
from . import views

urlpatterns = [
    path('fund/' , views.fundpage , name="fundpage"),
    path('fund/confirmationpage' , views.confirmationpage , name="confirmationpage"),

    
]