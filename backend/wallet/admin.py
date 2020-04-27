from django.contrib import admin
from .models import TaskerWallet, PaymentMethod, CustomerWallet

admin.site.register(PaymentMethod)
admin.site.register(TaskerWallet)
admin.site.register(CustomerWallet)

# Register your models here.
