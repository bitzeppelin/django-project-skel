# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
from admin import custom_admin

admin.autodiscover()

urlpatterns = patterns('',
        (r'^', include(admin.site.urls)),
        )

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$',
                serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
            url(r'^media/(?P<path>.*)$',
                serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            )

