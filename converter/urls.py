from django.conf.urls import patterns, url
from converter import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            url(r'^success$', views.success, name='success'),
            url(r'^error$', views.error, name='error'),
            url(r'^encoded$', views.encoding_uploaded, name='encoded'),
            url(r'^notify$', views.notify_encoded, name='notify_encoded'),
            url(r'^check_media$', views.check_media, name='check_media'),
            )

