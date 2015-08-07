from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('pages.urls')),
    url(r'^/$', include('pages.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^pages/', include('pages.urls')),
]
