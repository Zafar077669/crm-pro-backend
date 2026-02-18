from django.contrib import admin

# Register your models here.
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'status',
        'client',
        'owner',
        'assigned_to',
        'created_at',
    )
    list_filter = ('status', 'created_at')
    search_fields = ('title',)
