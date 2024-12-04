from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from ..models import AssetCountryModel, AssetLocationModel, LocationModel


@admin.register(AssetCountryModel)
class AssetCountryAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'country_name',
    )

    search_fields = (
        'country_name',
    )

    ordering = (
        'country_name',
    )

    readonly_fields = (
        'created',
        'updated',
    )

    fieldsets = (
        (_('Required Fields'), {
            'fields': (
                'country_name',
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


@admin.register(AssetLocationModel)
class AssetLocationAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    autocomplete_fields = (
        'asset',
    )

    search_fields = (
        'location__reference',
        'asset__name',
        'asset__es_name',
        'amount',
        'created_by__username',
        'created_by__email',
        'created_by__first_name',
        'created_by__last_name',
    )

    list_display = (
        'get_location_reference',
        'get_location_continent',
        'amount',
        'get_asset_es_name',
        'is_active',
    )

    list_display_links = list_display[:3]

    readonly_fields = (
        'created',
        'updated'
    )

    ordering = (
        'default_order',
        'created'
    )

    fieldsets = (
        (_('User Field'), {
            'fields': (
                'created_by',
            ),
        }),
        (_('Required Fields'), {
            'fields': (
                'asset',
                'location',
                'amount',
                'is_active'
            ),
        }),
        (_('Dates'), {
            'fields': (
                'created',
                'updated'
            ),
            'classes': (
                'collapse',
            )
        }),
        (_('Other fields'), {
            'fields': (
                'default_order',
            ),
            'classes': (
                'collapse',
            )
        }),
    )

    def get_asset_es_name(self, obj):
        return obj.asset.es_name

    def get_location_reference(self, obj):
        return obj.location.reference

    def get_location_continent(self, obj):
        return obj.location.get_continent_display()

    get_asset_es_name.short_description = _("spanish name")

    get_location_reference.short_description = _("reference")

    get_location_continent.short_description = _("continent")


@admin.register(LocationModel)
class LocationModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'reference',
        'continent',
        'country',
    )

    search_fields = (
        'reference',
        'continent',
        'country__country_name',
    )

    list_filter = (
        'continent',
        'is_active'
    )

    ordering = (
        'default_order',
        'reference',
        '-created'
    )

    readonly_fields = (
        'created',
        'updated'
    )

    fieldsets = (
        (_('User Field'), {
            'fields': (
                'created_by',
            ),
        }),
        (_('Required Fields'), {
            'fields': (
                'reference',
                'continent',
                'country',
                'is_active'
            )
        }),
        (_('Optional Fields'), {
            'fields': (
                'description',
            ),
            'classes': (
                'collapse',
            )
        }),
        (_('Dates'), {
            'fields': (
                'created',
                'updated'
            ),
            'classes': (
                'collapse',
            )
        }),
        (_('Other fields'), {
            'fields': (
                'default_order',
            ),
            'classes': (
                'collapse',
            )
        }),
    )
