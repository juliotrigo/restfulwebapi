# -*- coding: utf-8 -*-

"""views module of the website."""

from django.shortcuts import render


def home(request):
    """Home page."""
    return render(request, 'home.html')
