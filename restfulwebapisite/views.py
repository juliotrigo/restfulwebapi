from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    """Home page."""
    
    return render_to_response('home.xhtml',
                              context_instance=RequestContext(request))