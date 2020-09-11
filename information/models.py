from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Information(models.Model):
    description=models.CharField(max_length=500,unique=True)
    youtube=models.URLField(unique=True)
    title=models.CharField(max_length=500,unique=True)

    
class HomePage(models.Model):
    description=models.CharField(max_length=500,unique=True)
    youtube=models.URLField(unique=True)
    title=models.CharField(max_length=500,unique=True)
  
    

    

