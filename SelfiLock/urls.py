from django.conf.urls import patterns, include, url
#from profileAPI.views import IndexView, ProfileListAPIView
from django.contrib import admin
#from home.urls import urlpatterns as homeUrls

admin.autodiscover()

#from signup.views import api

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls), name ='admin'),
    url(r'^signup/','signup.views.api', name = 'signup'),
    url(r'^profile/',include('home.urls'), name = 'profile'),
    url(r'^$','home.views.home',name ='home'),
)