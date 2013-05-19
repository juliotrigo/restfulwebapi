# -*- coding: utf-8 -*-

"""cinema: film."""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cinema.models.commoninfo import CommonInfo

class Film(CommonInfo):
    
    """Film."""
    
    title = models.CharField(_("title"), max_length=100, help_text=_("Film title."))
    year = models.IntegerField(_("year"), help_text=_("Film release date."))
    running_length = models.IntegerField(_("running length"), help_text=_("Film duration."))
    
    def __unicode__(self):
        return self.title
    
    class Meta(CommonInfo.Meta):
        app_label = 'cinema'
        verbose_name = _('film')
        verbose_name_plural = _('films')
        index_together = [['year'],]
        ordering = ['title']

class OrderedFilm(Film):
    
    """Ordered film."""
    
    class Meta():
        proxy = True
        ordering = ['year']