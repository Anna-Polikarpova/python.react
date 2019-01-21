from django.contrib import admin

# Register your models here.
from .models import Item


@admin.register(Item)
class IDKAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
