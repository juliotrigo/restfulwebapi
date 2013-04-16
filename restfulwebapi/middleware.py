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
        try:
            #if settings.DEBUG:
            #    print('Accept: %s' % request.META['HTTP_ACCEPT'])
            #    print('Content-type: %s' % request.META['CONTENT_TYPE'])
            #    print('MIMETypeMiddleware process_request. ' + request.path)
            accept = request.META['HTTP_ACCEPT']
            content_type = request.META['CONTENT_TYPE']
        except KeyError:
            #return HttpResponse(content='Unsupported Media Type', content_type='text/html', status=415)
            return None
        
        return None
    
    def process_response(self, request, response):
        #if settings.DEBUG:
        #    print('MIMETypeMiddleware process_response. ' + request.path)
        return response