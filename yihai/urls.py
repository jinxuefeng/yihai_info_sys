from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from sales import urls as sales_url
from info import urls as info_url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoproj.views.home', name='home'),
    # url(r'^djangoproj/', include('djangoproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #DO NOT use r'^admin/$'
    url(r'', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include(sales_url)),
    url(r'^info/', include(info_url)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
)
