# -*- coding: utf-8 -*-

"""films views."""

from django.shortcuts import render_to_response
from django.http import Http404

from films.models import Film

def index(request):
    """Films main page."""
    return render_to_response('films/base_films.xhtml')

def films(request, id):
    """Shows either all films or an specific film."""
    try:
        if id is None:
            context = {'films': Film.objects.all()}
        else:
            list_of_films = []
            list_of_films.append(Film.objects.get(id=id))
            context = {'films': list_of_films}
            context.update({'id': id})
    except Film.DoesNotExist:
        raise Http404
    
    return render_to_response('films/films.xhtml', context)