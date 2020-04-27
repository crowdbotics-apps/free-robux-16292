from rest_framework import authentication
from location.models import TaskerLocation, MapLocation
from .serializers import TaskerLocationSerializer, MapLocationSerializer
from rest_framework import viewsets


class TaskerLocationViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerLocation.objects.all()


class MapLocationViewSet(viewsets.ModelViewSet):
    serializer_class = MapLocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MapLocation.objects.all()
