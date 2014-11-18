from django.db import models

# Create your models here.
class Signup(models.Model):
    email = models.CharField(max_length=50, blank=True, default='',primary_key=True)
    surname = models.CharField(max_length=30, blank=True, default='')
    name = models.CharField(max_length=30, blank=True, default='')
    image = models.CharField(max_length=500000, blank=True, default='');
    password = models.CharField(max_length=100, blank=True, default='')

class Achivement(models.Model):
    signup = models.ForeignKey(Signup)
    existe = models.BooleanField(default=False)