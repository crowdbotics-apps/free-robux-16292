from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskTransactionViewSet, RatingViewSet, MessageViewSet

router = DefaultRouter()
router.register("rating", RatingViewSet)
router.register("tasktransaction", TaskTransactionViewSet)
router.register("message", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
