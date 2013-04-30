# -*- coding: utf-8 -*-

"""Common information."""

from __future__ import unicode_literals

from django.db import models

from cinema.models import constants

class CommonInfo(models.Model):
    
    """Common information."""
    
    country = models.CharField(max_length=2, choices=constants.COUNTRY_CHOICES)
    
    class Meta:
        abstract = True