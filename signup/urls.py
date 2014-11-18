from django.conf.urls import url

from signup import views

urlpatterns = [
    url(r'^$', views.api, name='api'),
]