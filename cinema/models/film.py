# -*- coding: utf-8 -*-

"""Film."""

from __future__ import unicode_literals

from django.db import models

from cinema.models.commoninfo import CommonInfo

class Film(CommonInfo):
    
    """Film."""
    
    title = models.CharField(max_length=100)
    year = models.IntegerField(help_text="Film release date.")
    running_length = models.IntegerField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        app_label = 'films'
        index_together = [['year'],]
        ordering = ['title']

class OrderedFilm(Film):
    
    """Ordered film."""
    
    class Meta():
        ordering = ['year']
        proxy = True