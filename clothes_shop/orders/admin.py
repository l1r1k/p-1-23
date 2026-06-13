from django.contrib import admin
from .models import Order, PosOrder

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass