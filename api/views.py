#from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from api.models import Profile
from api.serializer import ProfileSerializer
from api.permissions import IsOwnerOrReadOnly


class ProfileMixin(object):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class ProfileViewSet(ProfileMixin, viewsets.ModelViewSet):
    pass


profile_router = DefaultRouter()
profile_router.register(r'profile',ProfileViewSet)
