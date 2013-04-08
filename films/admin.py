# -*- coding: utf-8 -*-

"""films admin."""

# Some other options
    #list_display
    #date_hierarchy
    #ordering
    #fields
    #filter_horizontal
    #filter_vertical
    #raw_id_fields

from django.contrib import admin

from films.models import Film
from films.models import Director
from films.models import FilmDirector

class FilmAdmin(admin.ModelAdmin):
    list_filter = ['year']
    search_fields = ['title']

class DirectorAdmin(admin.ModelAdmin):
    list_filter = ['name']

class FilmDirectorAdmin(admin.ModelAdmin):
    list_filter = ['director']

admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(FilmDirector, FilmDirectorAdmin)