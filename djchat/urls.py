from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home'),
    url(r'^', include('core.authentication.urls')),
    url(r'^chat/', include('core.urls')),
)
