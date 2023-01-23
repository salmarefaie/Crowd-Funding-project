from django.urls import path
from . import views

urlpatterns = [
    path('fundpage/' , views.fundpage , name="fundpage"),
    path('fundpage/confirmationpage' , views.confirmationpage , name="confirmationpage"),

]
app_name = 'fund'