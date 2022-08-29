from django.db import models

# Create your models here.

class donate(models.Model):
    name = models.CharField(max_length= 1000 , blank=True)
    amount = models.IntegerField()
    email=models.EmailField()