from django.contrib import admin
from .models import VisitorRecord

@admin.register(VisitorRecord)
class VisitorRecordAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'date', 'unique_visitors')
    list_filter = ('store_id', 'date')
    search_fields = ('store_id',)
    ordering = ('-date',)
