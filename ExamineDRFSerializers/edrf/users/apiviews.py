from django.contrib.auth import get_user_model
from rest_framework import viewsets
from edrf.users import serializers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
