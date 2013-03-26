# -*- coding: utf-8 -*-

"""Director."""

from django.db import models

from films.models.commoninfo import CommonInfo

class Director(CommonInfo):
    
    """Director."""
    
    name = models.CharField(max_length=80)
    film = models.ManyToManyField('Film', through='FilmDirector')
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = 'films'

class FilmDirector(models.Model):
    
    """Films of directors."""
    
    film = models.ForeignKey('Film')
    director = models.ForeignKey('Director')
    
    def __unicode__(self):
        return self.film + " by " + self.director
    
    class Meta:
        app_label = 'films'
        db_table = 'films_film_director'
        verbose_name = 'Film of director'
        verbose_name_plural = 'Films of directors'
        unique_together = ('film', 'director',)