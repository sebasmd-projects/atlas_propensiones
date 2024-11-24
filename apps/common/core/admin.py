from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'last_name', 'email',
        'subject', 'message', 'created'
    )
    search_fields = ('name', 'last_name', 'email', 'subject', 'message')
    list_filter = ('is_active',)
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'last_name', 'email', 'subject', 'message')
        }),
        ('Important dates', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )
