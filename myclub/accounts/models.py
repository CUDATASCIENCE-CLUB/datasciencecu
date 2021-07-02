from django.db import models
from django.contrib.auth.models import User


class member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True,default='images/logo1.jpg')
    matno = models.CharField(max_length=10)

class Admin(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', null=True)

