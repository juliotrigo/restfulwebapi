from django.db import models

# Create your models here.

class Director(models.Model):
    
    """Director"""
    
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    
class Film(models.Model):
    
    """Film"""
    
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.ManyToManyField(Director, through='FilmDirector')

class FilmDirector(models.Model):
    
    """film_director many-to-many"""
    
    film = models.ForeignKey(Film)
    director = models.ForeignKey(Director)
    
    class Meta:
        db_table = 'films_film_director'
        unique_together = ('film', 'director',)