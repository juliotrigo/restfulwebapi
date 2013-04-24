# -*- coding: utf-8 -*-

"""Middleware."""

from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse
from django.conf import settings

class MIMETypeMiddleware(object):

    """MIME Type Middleware."""

    def __init__(self):
        pass
        #if settings.DEBUG:
        #    print('MIMETypeMiddleware initiated.')
    
    def process_request(self, request):
        #try:
        #    accept = request.META['HTTP_ACCEPT']
        #    content_type = request.META['CONTENT_TYPE']
        #    if settings.DEBUG:
        #        print('Accept: %s' % accept)
        #        print('Content-type: %s' % content_type)
        #        print('MIMETypeMiddleware process_request. ' + request.path)
        #except KeyError:
        #    return HttpResponse(content='Unsupported Media Type', content_type='text/html', status=415)
        
        return None
    
    def process_response(self, request, response):
        #if settings.DEBUG:
        #    print('MIMETypeMiddleware process_response. ' + request.path)
        #    print('Content-type: %s' % response['Content-Type'])
        #Content-Type: application/prs.restfulwebapi+xml; charset=utf-8; version=1.0
        #Vary: Content-Type
        return response