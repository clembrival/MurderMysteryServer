from django.conf.urls import patterns, url
from killerapp import views


urlpatterns = patterns('',
                       url(r'^count/$', views.get_count, name='get_count'),
                       url(r'^file/$', views.get_file, name='get_file'),
                       url(r'^update/$', views.update, name='update_file'),
                       )
