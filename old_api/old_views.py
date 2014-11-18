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


"""
profile_list = ProfileViewSet.as_view({
    'get':'list',
    'post':'create',
    })

profile_detail = ProfileViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
    })

"""


"""
class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileMixin(object):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
"""


"""
@api_view(['GET','POST'])
def profile_list(request):
    if request.method = 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles)
        return Response(serializer.data)

    elif request.method = 'POST':
        serializer = ProfileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def profile_detail(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""