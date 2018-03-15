from django.contrib.auth import get_user_model
from rest_framework import serializers as rest_serializers
from edrf.profiles.models import Profile
from edrf.profiles.serializers import ProfileSerializer

class UserSerializer(rest_serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'is_staff', 'profile',)

    # DRF cannot create the nested serializer automatically
    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('profile')
        new_user = get_user_model().objects.create(**validated_data)
        print(new_user)
        new_user.save()
        profile = Profile.objects.filter(user_id=new_user.id)
        print(profile)
        role_name = profile_data.pop('get_role_display')
        role_dict = dict((y.upper(), x) for x, y in Profile.ROLE_CHOICES)
        print(role_dict)
        role_id = role_dict[role_name.upper()]
        print("role id", role_id)
        profile_data['role'] = role_id
        print(profile_data)
        profile.update(**profile_data)
        new_user.profile = profile.first()
        return new_user
