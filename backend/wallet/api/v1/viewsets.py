from rest_framework import authentication
from wallet.models import TaskerWallet, PaymentMethod, CustomerWallet
from .serializers import (
    TaskerWalletSerializer,
    PaymentMethodSerializer,
    CustomerWalletSerializer,
)
from rest_framework import viewsets


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class TaskerWalletViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerWallet.objects.all()


class CustomerWalletViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerWallet.objects.all()
