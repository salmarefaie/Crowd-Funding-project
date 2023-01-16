from django.db import models

# Create your models here.
class Order(models.Model):
    data_created = models.DateTimeField(auto_now_add=True, null=True)
