from django.db import models

class userInfo(models.Model):
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

# Create your models here.
