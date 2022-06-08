import email
from click import password_option
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key= True)
    username = models.TextField()
    email= models.TextField()
    password = models.TextField()
    masterpassword = models.TextField()

class Password(models.Model):
    id = models.AutoField(primary_key= True)
    user_id = models.IntegerField()
    username = models.TextField()
    email = models.TextField()
    destination_url = models.TextField()
    password = models.TextField()
