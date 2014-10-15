from django.conf.urls import patterns, include, url
#from profileAPI.views import IndexView, ProfileListAPIView
from django.contrib import admin
admin.autodiscover()

from api.views import profile_router


urlpatterns = patterns('',
    # Examples:
    url(r'^api/', include(profile_router.urls), name ='api'),
    #url(r'^api/', include('api.urls'), name ='api'),
    url(r'^admin/', include(admin.site.urls), name ='admin'),
    
    #url(r'^$','story.views.home',name ='home'),

)
