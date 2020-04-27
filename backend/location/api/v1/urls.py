from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskerLocationViewSet, MapLocationViewSet

router = DefaultRouter()
router.register("taskerlocation", TaskerLocationViewSet)
router.register("maplocation", MapLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
