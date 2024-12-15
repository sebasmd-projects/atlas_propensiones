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
    list_per_page = 100
    max_list_per_page = 2000

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['list_per_page_options'] = [10, 50, 100, 1000]

        list_per_page_value = request.GET.get('list_per_page')
        if list_per_page_value:
            try:
                list_per_page_value = int(list_per_page_value)
                if list_per_page_value > self.max_list_per_page:
                    messages.warning(
                        request,
                        f"Máximo permitido: {self.max_list_per_page} registros."
                    )
                    list_per_page_value = self.max_list_per_page
                elif list_per_page_value < 1:
                    messages.warning(request, "Mínimo permitido: 1 registro.")
                    list_per_page_value = 1
                self.list_per_page = list_per_page_value
            except ValueError:
                messages.error(request, "Por favor, ingrese un número válido.")
        return super().changelist_view(request, extra_context=extra_context)

    def detail_link(self, obj):
        url = reverse('certificates:detail', args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, obj.pk)


admin.site.register(CertificateModel, CertificateAdmin)
