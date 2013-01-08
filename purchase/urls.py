from django.conf.urls.defaults import *
from rest_framework.urlpatterns import format_suffix_patterns
from info import views

urlpatterns = patterns(
    '',
    (r'org/$', views.OrgList.as_view()),
    (r'contact/$', views.ContactList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
