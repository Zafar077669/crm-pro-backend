from django.contrib import admin

# Register your models here.
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'lead',
        'amount',
        'currency',
        'stage',
        'owner',
        'created_at',
    )
    list_filter = ('stage', 'currency')
