from django.db import models

class Town(models.Model):
    name = models.CharField(max_length=30)
class Gymnasium(models.Model):
    name = models.CharField(max_length=30)
class Key(models.Model):
    number = models.IntegerField()
class Post(models.Model):
    name = models.CharField(max_length=30)
class Board(models.Model):
    year = models.IntegerField()
class School(models.Model):
    name = models.CharField(max_length=30)
class StudyLine(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School)
class Study(models.Model):
    studyLine = models.ForeignKey(StudyLine)
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    graduated = models.BooleanField()
    active = models.BooleanField()
class MedlemsAvgifter(models.Model):
    betald = models.CharField(max_length=30,null=True)
class MedlemsTyp(models.Model):
    medlemsTyper = (('ordinarieMedlem','Ordinarie Medlem'),('extraMedlem','Extra Medlem'))
    aldreMedlem = models.BooleanField();
class User(models.Model):
    type        = models.CharField(max_length=30)
    phone       = models.CharField(max_length=20)
    email       = models.EmailField(max_length=30)
    adress      = models.CharField(max_length=30)
    firstName   = models.CharField(max_length=30)
    lastName    = models.CharField(max_length=30)
    postcode    = models.CharField(max_length=10)
    city        = models.CharField(max_length=30)
    homeTown    = models.ForeignKey(Town)
    study       = models.ForeignKey(Study)
    gymnasium   = models.ForeignKey(Gymnasium)
    MedlemsAvgift = models.ForeignKey(MedlemsAvgifter, null=True)
    #key         = models.ForeignKey(Key)
class Funktunar(models.Model):
    post    = models.ForeignKey(Post)
    year    = models.IntegerField(null=True)
    board   = models.ForeignKey(Board)
    user    = models.ForeignKey(User)
# Create your models here.
