from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'owner', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-created_at',)
