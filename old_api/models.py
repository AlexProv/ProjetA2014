from django.db import models

class Profile(models.Model):
    owner = models.ForeignKey('auth.User',related_name='profile')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, default='')
    age = models.IntegerField()
    eyesColor = models.CharField(max_length=30)
    hairColor = models.CharField(max_length=30)

class UsersLocation(models.Model):
    location = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, related_name='UsersLocations')
