# -*- coding: utf-8 -*-

"""films admin."""

from django.contrib import admin

from films.models import Film
from films.models import OrderedFilm
from films.models import Director
from films.models import FilmDirector

admin.site.register(Film)
admin.site.register(OrderedFilm)
admin.site.register(Director)
admin.site.register(FilmDirector)