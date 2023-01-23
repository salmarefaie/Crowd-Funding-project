from django.urls import path
from . import views

urlpatterns = [
    path('entrypage/confirmationpage' , views.confirmationpage , name="confirmationpage"),
    path('entrypage/' , views.CreateFund , name="entrypage"),


]
app_name = 'fund'