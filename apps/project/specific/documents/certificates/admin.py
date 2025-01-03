from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.common.utils.admin import GeneralAdminModel

from .models import CertificateModel


class CertificateAdmin(GeneralAdminModel):
    list_display = (
        'user',
        'name',
        'last_name',
        'document_type',
        'document_number',
        'approved',
        'approval_date',
        'detail_link',
        'created',
        'updated'
    )
    list_display_links = list_display[:4]
    search_fields = (
        'id',
        'name',
        'last_name',
        'document_type',
        'document_number',
        'document_number_hash',
    )
    list_filter = ("is_active", "approved", "document_type")
    fieldsets = (
        (_('Certificate'), {'fields': (
            'user',
            'name',
            'last_name',
            'document_type',
            'document_number',
            'document_number_hash',
            'is_active',
            'approved',
            'approval_date'
        )}),
        (_('Dates'), {'fields': (
            'created',
            'updated'
        )}),
        (_('Priority'), {'fields': (
            'default_order',
        )}),
    )
    readonly_fields = (
        'created',
        'updated',
        'document_number_hash',
    )

    def detail_link(self, obj):
        url = reverse('certificates:detail', args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, obj.pk)


admin.site.register(CertificateModel, CertificateAdmin)
