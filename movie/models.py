from django.db import models
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

class Suggest(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
