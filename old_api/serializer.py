from rest_framework import serializers 

from api.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    owner = serializers.Field('owner.username')

    class Meta: 
        model = Profile
        fields = ('name', 'age', 'eyesColor', 'hairColor', 'owner',)
