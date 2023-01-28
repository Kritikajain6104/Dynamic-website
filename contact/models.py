from django.db import models

# Create your models here.
class contact1(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    message=models.CharField(max_length=200)