from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True, null=True)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=51)


# Create your models here.
