from django.db import models


# Create your models here.
class Event(models.Model):
    username=models.CharField(max_length=50,null=False)
    firstname=models.CharField(max_length=150,null=False)
    lastname=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=150,null=False)
    password=models.CharField(max_length=150,null=False)    
