from django.contrib import admin
from .models import CustomerProfile, TaskerProfile, Notification

admin.site.register(CustomerProfile)
admin.site.register(TaskerProfile)
admin.site.register(Notification)

# Register your models here.
