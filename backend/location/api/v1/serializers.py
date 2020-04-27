from rest_framework import serializers
from location.models import TaskerLocation, MapLocation


class TaskerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerLocation
        fields = "__all__"


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = "__all__"
