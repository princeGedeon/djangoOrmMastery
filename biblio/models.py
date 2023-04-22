from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    nom=models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)

class Tag(models.Model):
    title=models.CharField(max_length=200)

class Book(models.Model):
    title=models.CharField(max_length=200)
    autor=models.ForeignKey(Author,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)
    price=models.DecimalField(max_digits=9999,decimal_places=2,default=100)