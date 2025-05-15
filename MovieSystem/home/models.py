# Create your models here.
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
