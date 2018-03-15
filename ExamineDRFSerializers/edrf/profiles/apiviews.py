from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from edrf.profiles import serializers
from edrf.profiles.models import Profile

# ViewSets define the view behavior.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'head']
