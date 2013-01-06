from django.conf.urls.defaults import *

urlpatterns = patterns(
    'sales.views',
    (r'^$', 'index'),
    (r'^(?P<object_id>\d+)/$', 'detail'),
)
