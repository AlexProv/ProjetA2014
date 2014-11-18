from django.conf.urls import patterns, include, url
#from profileAPI.views import IndexView, ProfileListAPIView
from django.contrib import admin

admin.autodiscover()

#from signup.views import api

urlpatterns = patterns('',
    # Examples:

    #url(r'^api/', include(profile_router.urls), name ='api'),
    #url(r'^api/', include('api.urls'), name ='api'),
    url(r'^admin/', include(admin.site.urls), name ='admin'),
    url(r'^signup/','signup.views.api', name = 'signup'),
    url(r'^$','home.views.home',name ='home'),
)