from django.db import models

class Town(models.Model):
    name = models.CharField 

class Key(models.Model):
    number = models.IntegerField

class Post(models.Model):
    name = models.CharField

class Board(models.Model):
    year = models.CharField


class User(models.Model):
    type        = models.CharField
    email       = models.EmailField
    adress      = models.CharField
    firstName   = models.CharField
    lastName    = models.CharField
    homeTown    = models.ForeignKey(Town)
    key         = models.ForeignKey(Key)

class Funktunar(models.Model):
    post    = models.ForeignKey(Post)
    year    = models.IntegerField
    board   = models.ForeignKey(Board)
    user    = models.ForeignKey(User)
# Create your models here.
