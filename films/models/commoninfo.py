# -*- coding: utf-8 -*-

"""Common information."""

from django.db import models

from films.models import constants

class CommonInfo(models.Model):
    
    """Common information."""
    
    country = models.CharField(max_length=2, choices=constants.COUNTRY_CHOICES)
    
    class Meta:
        abstract = True