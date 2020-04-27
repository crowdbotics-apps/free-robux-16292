from rest_framework import authentication
from task.models import TaskTransaction, Rating, Message
from .serializers import TaskTransactionSerializer, RatingSerializer, MessageSerializer
from rest_framework import viewsets


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rating.objects.all()


class TaskTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TaskTransactionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskTransaction.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Message.objects.all()
