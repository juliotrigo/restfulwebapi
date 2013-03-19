# Create your views here.

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('films/base_films.xhtml')
