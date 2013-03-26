# -*- coding: utf-8 -*-

"""Film."""

from django.db import models

from films.models.commoninfo import CommonInfo

class Film(CommonInfo):
    
    """Film."""
    
    title = models.CharField(max_length=100)
    year = models.IntegerField(help_text="Film release date.")
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        app_label = 'films'
        index_together = [['year'],]

class OrderedFilm(Film):
    
    """Ordered film."""
    
    class Meta():
        ordering = ['year']
        proxy = True