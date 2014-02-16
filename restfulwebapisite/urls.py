# -*- coding: utf-8 -*-

"""urls module of the website."""

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'restfulwebapisite.views.home', name='home'),
    # url(r'^restfulwebapisite/', include('restfulwebapisite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^cinema/', include('cinema.urls', namespace='cinema', app_name='cinema')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts', app_name='accounts')),

    #url(r'^i18n/', include('django.conf.urls.i18n')),
)

# Copied and changed from django.conf.urls.i18n
urlpatterns += patterns('',
    url(r'^i18n/setlang/$', 'accounts.views.custom_i18n', name='set_language'),
)
