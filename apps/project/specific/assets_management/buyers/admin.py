from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from apps.project.specific.assets_management.buyers.models import OfferModel


@admin.register(OfferModel)
class OfferModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    autocomplete_fields = (
        'created_by',
        'asset',
        'buyer_country',
    )
    
    list_display = (
        'created_by',
        'asset',
        'offer_type',
        'quantity_type',
        'is_active',
        'is_approved',
    )

    search_fields = (
        'created_by',
        'asset',
        'offer_type',
        'quantity_type',
        'is_active',
    )

    readonly_fields = (
        'created',
        'updated',
    )

    fieldsets = (
        (_('Required Fields'), {
            'fields': (
                'created_by',
                'asset',
                'offer_type',
                'quantity_type',
                'offer_amount',
                'offer_quantity',
                'buyer_country',
                'es_procedure',
                'en_procedure',
                
            ),
        }),
        (_('Approval'), {
            'fields': (
                'approved_by',
                'is_approved',
                'is_active',
            ),
        }),
        (_('Banner Image'), {
            'fields': (
                'es_banner',
                'en_banner',
            ),
            'classes': (
                'collapse',
            ),
        }),
        (_('Dates'), {
            'fields': (
                'created',
                'updated',
            ),
            'classes': (
                'collapse',
            ),
        }),
    )
