# -*- coding: utf-8 -*-

"""cinema: director."""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cinema.models.commoninfo import CommonInfo


class Director(CommonInfo):

    """Director."""

    name = models.CharField(_("name"), max_length=80, help_text=_("Director's name."))
    film = models.ManyToManyField('Film', through='FilmDirector', verbose_name=_("film"))

    def __unicode__(self):
        return self.name

    class Meta(CommonInfo.Meta):
        app_label = 'cinema'
        verbose_name = _('director')
        verbose_name_plural = _('directors')


class FilmDirector(models.Model):

    """Films of directors."""

    film = models.ForeignKey('Film', verbose_name=_("film"), related_name='films')
    director = models.ForeignKey('Director', verbose_name=_("director"), related_name='directors')

    def __unicode__(self):
        # Translators: Film by director
        return _('%(film)s by %(director)s') % {'film': self.film, 'director': self.director}

    class Meta:
        app_label = 'cinema'
        db_table = 'cinema_film_director'
        verbose_name = _('film of director')
        verbose_name_plural = _('films of directors')
        unique_together = ('film', 'director',)
