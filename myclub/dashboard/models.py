from django.db import models
from django.contrib.auth.models import User

class events(models.Model):
    name = models.CharField(max_length=30)
    time = models.TimeField(auto_created=True,null=True)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True)
    links = models.CharField(max_length=50)
    date=models.DateField(auto_created=True,null=True)

class thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_created=True, null=True)

class replies(models.Model):
    user = models.CharField(max_length=30)
    comment = models.CharField(max_length=1000)
    tread = models.ForeignKey(thread, on_delete=models.CASCADE, null=False)
