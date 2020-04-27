from django.contrib import admin
from .models import TaskTransaction, Rating, Message

admin.site.register(Rating)
admin.site.register(TaskTransaction)
admin.site.register(Message)

# Register your models here.
