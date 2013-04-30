from django.conf.urls import patterns, url

urlpatterns = patterns('cinema',
    url(r'^$', 'views.index', name='index'),
    url(r'^films/$', 'views.films', {'id': None}, name='films_all'),
    url(r'^films/(?P<id>\d+)/$', 'views.films', name='films_id')
)