# -*- coding: utf-8 -*-

"""cinema views."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

from cinema.models import Film


@login_required
def index(request):
    """Cinema main page."""
    return render(request, 'cinema/base_cinema.html')


@login_required
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

    return render(request, 'cinema/films.html', dictionary=context)
