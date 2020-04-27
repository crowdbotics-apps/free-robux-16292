from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomerProfileViewSet, TaskerProfileViewSet, NotificationViewSet

router = DefaultRouter()
router.register("customerprofile", CustomerProfileViewSet)
router.register("taskerprofile", TaskerProfileViewSet)
router.register("notification", NotificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
