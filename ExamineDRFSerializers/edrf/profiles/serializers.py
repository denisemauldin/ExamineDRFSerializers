from rest_framework import serializers as rest_serializers
from rest_framework.exceptions import APIException
from edrf.profiles.models import Profile

class ProfileSerializer(rest_serializers.ModelSerializer):
    role = rest_serializers.CharField(source='get_role_display')
    names = rest_serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('location', 'birthdate', 'role', 'names',)

    def get_names(self, obj):
        return dict((y, x) for x, y in obj.ROLE_CHOICES).keys()

    def create(self, validated_data):
        raise APIException('Profile is created by User')

    def update(self, instance, validated_data):
        data = copy.deepcopy(validated_data)
        instance = self.update_instance(instance, validated_data)
        return instance



