from django.conf import settings
from django.db import models


class Rating(models.Model):
    "Generated Model"
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="rating_tasker",
    )
    rating = models.FloatField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    review = models.TextField(null=True, blank=True,)
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rating_customer",
    )


class TaskTransaction(models.Model):
    "Generated Model"
    price = models.FloatField()
    status = models.CharField(max_length=10,)
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    tip = models.FloatField(null=True, blank=True,)
    timestamp_arrived = models.DateTimeField(null=True, blank=True,)
    timestamp_completed = models.DateTimeField(null=True, blank=True,)
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tasktransaction_customer",
    )
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tasktransaction_tasker",
    )
    location = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tasktransaction_location",
    )
    subcategory = models.ForeignKey(
        "task_category.Subcategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tasktransaction_subcategory",
    )


class Message(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "task_profile.CustomerProfile",
        on_delete=models.CASCADE,
        related_name="message_customer",
    )
    tasker = models.ForeignKey(
        "task_profile.TaskerProfile",
        on_delete=models.CASCADE,
        related_name="message_tasker",
    )
    message = models.TextField()
    timestamp_created = models.DateTimeField(auto_now_add=True,)
    task = models.ForeignKey(
        "task.TaskTransaction",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message_task",
    )


# Create your models here.
