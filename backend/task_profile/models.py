from django.conf import settings
from django.db import models


class CustomerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="customerprofile_user",
    )
    mobile_number = models.CharField(max_length=20,)
    photo = models.URLField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    last_updated = models.DateTimeField(auto_now=True,)
    last_login = models.DateTimeField(null=True, blank=True,)


class TaskerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="taskerprofile_user",
    )
    mobile_number = models.CharField(max_length=20,)
    photo = models.URLField()
    subcategory = models.ManyToManyField(
        "task_category.Subcategory", related_name="taskerprofile_subcategory",
    )
    is_available = models.BooleanField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    last_updated = models.DateTimeField(auto_now=True,)
    last_login = models.DateTimeField(null=True, blank=True,)


class Notification(models.Model):
    "Generated Model"
    type = models.CharField(max_length=20,)
    message = models.TextField()
    user = models.ManyToManyField("users.User", related_name="notification_user",)
    timestamp_created = models.DateTimeField(auto_now_add=True,)


# Create your models here.
