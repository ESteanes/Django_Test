from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50,blank=False,default='')
    captial = models.CharField(max_length=100,blank=False,default='')


# Create your models here.
