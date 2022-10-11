from django.db import models

# Create your models here.

class donate(models.Model):
    name = models.CharField(max_length= 1000 , blank=True)
    amount = models.IntegerField()
    email=models.EmailField()


class UserEnqFrom(models.Model):
    email = models.EmailField()
    name=models.CharField(max_length=200, unique=True)
    message=models.TextField()