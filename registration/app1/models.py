from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()


class customer(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  

