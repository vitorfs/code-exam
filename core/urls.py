# coding: utf-8
from django.conf.urls import patterns, include, url
from core.views import Homepage


urlpatterns = patterns('eventex.core.views',
    url(r'^$', Homepage.as_view(), name='homepage'),
)