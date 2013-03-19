from django.conf.urls import patterns, url

from films import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)