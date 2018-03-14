from django.conf.urls import include, url
from rest_framework import permissions, routers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound

import edrf.users.apiviews as user_views


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@permission_classes([permissions.AllowAny])
def not_found(request):
    raise NotFound()

class EDRFRouter(routers.DefaultRouter):
    pass

router = EDRFRouter()

router.register (r'users', user_views.UserViewSet, 'users')
