from django.db import models

# Create your models here.
class user(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Mobile_Phone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.First_Name + " " +self.Last_Name

    class Meta:
        verbose_name= "USERS"