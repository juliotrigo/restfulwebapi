from django.db import models

FRANCE = 'FR'
SPAIN = 'ES'
ITALY = 'IT'
US = 'US'
UK = 'UK'
COUNTRY_CHOICES = (
    (FRANCE, 'France'),
    (SPAIN, 'Spain'),
    (ITALY, 'Italy'),
    (US, 'United States'),
    (UK, 'United Kingdom'),
)

class Director(models.Model):
    
    """Director"""
    
    #blank
    #null
    #default
    #editable
    #help_text
    #primary_key
    #unique
    #verbose_name
    
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    
    def __unicode__(self):
        return self.name
    
class Film(models.Model):
    
    """Film"""
    
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    director = models.ManyToManyField(Director, through='FilmDirector')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        index_together = [['year'],]

class FilmDirector(models.Model):
    
    """Film_Director many-to-many"""
    
    film = models.ForeignKey(Film)
    director = models.ForeignKey(Director)
    
    def __unicode__(self):
        return self.film + " by " + self.director
    
    class Meta:
        db_table = 'films_film_director'
        verbose_name = 'Film of director'
        verbose_name_plural = 'Films of directors'
        unique_together = ('film', 'director',)