from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    small_description = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2)
    target_launch_date = models.DateField(null=True, blank=True)
    create_project_date = models.DateTimeField(default=datetime.now)
    total_fund = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=None,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "all projects"