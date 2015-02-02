from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^converter/', include('converter.urls')),
    url(r'^', include('converter.urls')),
)
