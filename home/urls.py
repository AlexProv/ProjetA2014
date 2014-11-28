from django.conf.urls import patterns, url

from home.views import profile,home,landing,tester

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^profile/(?P<email>[\w.@+-]+)/$', profile, name='profile'),
    url(r'^profile/', landing, name='landing'),
    url(r'^simon/', tester, name='tester'),
)