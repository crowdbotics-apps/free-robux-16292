from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskerWalletViewSet, PaymentMethodViewSet, CustomerWalletViewSet

router = DefaultRouter()
router.register("paymentmethod", PaymentMethodViewSet)
router.register("taskerwallet", TaskerWalletViewSet)
router.register("customerwallet", CustomerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
