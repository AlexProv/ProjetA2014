from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

#from api.views import ProfileList, ProfileDetail
from api.views import profile_list, profile_detail

urlpatterns = patterns(
    'api.views',
    #url(r'^profile/$','profile_list', name = 'profile_list'),
    #url(r'^profile/(?<pk>[0-9]+)$','profile_details', name = 'profile_details'),
    url(r'^profile/$', profile_list,name = 'profile_list'),
    url(r'^profile/(?P<pk>[0-9]+)$', profile_detail, name = 'profile_detail'),
)