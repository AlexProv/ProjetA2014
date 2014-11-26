from django.conf.urls import patterns, url

from home.views import profile,home,simon

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^profile/', profile, name='profile'),
    url(r'^simon/', simon, name='profile'),
)