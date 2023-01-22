from django.db import models

class fund(models.Model):
    projectname = models.CharField(max_length=50 , verbose_name="project name")
    username = models.CharField(max_length=50 , verbose_name="user name")
    useremail = models.CharField(max_length=50 , verbose_name="user email")

    def __str__(self):
        return self.username
    class Meta:
        verbose_name= "fund information"