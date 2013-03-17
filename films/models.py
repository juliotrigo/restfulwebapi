from django.db import models

# Create your models here.

class Film(models.Model):
    
    """Film"""
    
    title = models.CharField(max_length=50)
    year = models.IntegerField()
