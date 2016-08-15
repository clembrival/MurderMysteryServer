from django.conf.urls import patterns, url
from killerapp import views


urlpatterns = patterns('',
                       url(r'^timestamp/$', views.get_timestamp, name='get_timestamp'),
                       url(r'^new_entries/$', views.get_new_entries, name='get_new_entries'),
                       url(r'^update/$', views.update, name='update_file'),
                       )
