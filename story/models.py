from django.db import models

# Create your models here.

class Line(models.Model):
    text = models.CharField(max_length=255)