import email
from click import password_option
from django.db import models

# Create your models here.

#null = true para que no sea obligatorio el campo en la base de datos
#blank = true para que no sea obligatorio rellenarlo en el formulario

class User(models.Model):
    id = models.AutoField(primary_key= True)
    username = models.TextField(max_length=100)
    email= models.TextField(max_length=100)
    user_password = models.TextField(max_length=100, null=False, default=str(username)) # password for authentication
    masterpassword = models.TextField(max_length=300) # password for encryption

    def __str__(self):
        return self.username

class Password(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    username = models.TextField(max_length=100)
    email = models.EmailField()
    destination_url = models.URLField()
    password = models.TextField()

    def __str__(self):
        return self.destination_url
