from django.db import models

class Town(models.Model):
    name = models.CharField(max_length=30,default='loviisa') 
class Gymnasium(models.Model):
    name = models.CharField(max_length=30)
class Key(models.Model):
    number = models.IntegerField(null=True)

class Post(models.Model):
    name = models.CharField(max_length=30)

class Board(models.Model):
    year = models.IntegerField(null=True)

class School(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    type        = models.CharField(max_length=30)
    email       = models.EmailField()
    adress      = models.CharField(max_length=30)
    firstName   = models.CharField(max_length=30)
    lastName    = models.CharField(max_length=30)
    study       = models.CharField(max_length=30)
    postcode    = models.CharField(max_length=10)
    homeTown    = models.ForeignKey(Town)
#    key         = models.ForeignKey(Key)

class Funktunar(models.Model):
    post    = models.ForeignKey(Post)
    year    = models.IntegerField(null=True)
    board   = models.ForeignKey(Board)
    user    = models.ForeignKey(User)
# Create your models here.
