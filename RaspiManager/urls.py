from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from tastypie.api import Api
from api import CollectionResource
v1_api = Api(api_name='v1')
v1_api.register(CollectionResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'www.views.home', name='home'),
    url(r'^template/(?P<template_name>[\w\d\-\_\/]*)', 'www.views.template'),

    # Module URLS
    url(r'^modules$', 'www.views.modules.index', name='modules'),


    # Management URLS
    url(r'^manage/system$', direct_to_template, {'template': 'manage/system.html'}, name='manage_system'),
    url(r'^manage/media$', 'www.views.media.manage_media', name='manage_media'),

    # System Management
    url(r'^system/?$', direct_to_template, {'template': 'manage/system/index.html'}),
    url(r'^system/users$', direct_to_template, {'template': 'manage/system/users.html'}),
    url(r'^system/network$', direct_to_template, {'template': 'manage/system/network.html'}),

    url(r'^system/drives$', direct_to_template, {'template': 'manage/system/drives.html'}),


    # Media Management
    url(r'^media/settings$', 'www.views.media.settings', name="minidlna_settings"),
    url(r'^media/collections$', direct_to_template, {'template': 'manage/collections/index.html'}),
    url(r'^media/collections/create$', 'www.views.media.collection'),
    url(r'^media/collections/edit/(?P<collection_id>\d+)$', 'www.views.media.collection'),

    # Documentation URLS
    url(r'^docs/walkthroughs$', 'www.views.docs.walkthroughs', name='walkthroughs'),
    # url(r'^RaspiManager/', include('RaspiManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # API urls
    url(r'^api/file_tree$', 'api.views.file_tree', name='file_tree'),
    url(r'^api/system/(?P<command>[\w\.]+)', 'api.views.system.run_command', name='command'),
    (r'^api/', include(v1_api.urls)),
)
