from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.chat'),
    url(r'^message/$', 'core.views.publishMessage'),
)
