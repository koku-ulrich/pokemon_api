from rest_framework.pagination import PageNumberPagination
from django.db import models
import pandas as pd

class Pokemon(models.Model):
    id = models.CharField(max_length=3,primary_key=True, unique=True)
    name = models.CharField(max_length=30,unique=True, null=False, blank=False)
    type1 = models.CharField(max_length=25,blank=True, null=True)
    type2 = models.CharField(max_length=25,blank=True, null=True)
    image_url = models.URLField(null=False)
    total = models.IntegerField(default=0,blank=True, null=True)
    hp = models.IntegerField(default=0,blank=True, null=True)
    attack = models.IntegerField(default=0,blank=True, null=True)
    defense = models.IntegerField(default=0,blank=True, null=True)
    sp_atk = models.IntegerField(default=0,blank=True, null=True)
    sp_def = models.IntegerField(default=0,blank=True, null=True)
    speed = models.IntegerField(default=0,blank=True, null=True)
    generation = models.IntegerField(default=0,blank=True, null=True)
    legendary =  models.BooleanField(default = False, blank = True)

class Type(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30,unique=True, null=False, blank=False)