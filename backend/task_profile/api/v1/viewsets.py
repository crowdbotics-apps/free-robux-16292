from rest_framework import authentication
from task_profile.models import CustomerProfile, TaskerProfile, Notification
from .serializers import (
    CustomerProfileSerializer,
    TaskerProfileSerializer,
    NotificationSerializer,
)
from rest_framework import viewsets


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerProfile.objects.all()


class TaskerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerProfile.objects.all()


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Notification.objects.all()
