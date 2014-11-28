from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50, blank=True, default='',primary_key=True)
    surname = models.CharField(max_length=30, blank=True, default='')
    name = models.CharField(max_length=30, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')


class AchivementsManager(models.Model):
    signup = models.ForeignKey(Signup)
    name = models.CharField(max_length=30, blank=True, default='')

class Achivement(models.Model):
    manager = models.ForeignKey(AchivementsManager)
    name = models.CharField(max_length=30, blank=True, default='')
    unlocked = models.CharField(max_length=5,default='False')
    description = models.CharField(max_length=400, blank=True, default='')

class Stats(models.Model):
    signup = models.ForeignKey(Signup)
    numbersOfWin = models.CharField(max_length=50, blank=True, default='')
    numbersOfFail = models.CharField(max_length=50, blank=True, default='')
    timesPlayed = models.CharField(max_length=50, blank=True, default='')
    achivementsUnlocked = models.CharField(max_length=50, blank=True, default='')

class Locations(models.Model):
    signup = models.ForeignKey(Signup)
    lat = models.CharField(max_length=100, blank=True, default='')
    lng = models.CharField(max_length=100, blank=True, default='')



