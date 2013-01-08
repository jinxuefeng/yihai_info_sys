from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#auto find and run admin.py in each app
admin.autodiscover()
from sales import urls as sales_url
from views import *

#urlpatterns is a tuple with elements as: (regular expression, Python callback function [, optional dictionary])
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproj.views.home', name='home'),
    # url(r'^djangoproj/', include('djangoproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #DO NOT use r'^admin/$'
    url(r'^$', home),
    url(r'^log_in/$', log_in),
    url(r'^log_out/$', log_out),
    url(r'^my_deck/$', my_deck),
    url(r'^static/(?P<path>.*)','django.views.static.serve', 
        {'document_root': '/home/jinxuefeng/yihai_info_sys/yihai/static'}),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
)
