
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from ..models import AssetCategoryModel, AssetModel, AssetsNamesModel
from .filters import (HasImageFilter, QuantityTypeFilter,
                      ZeroTotalQuantityFilter)


@admin.register(AssetsNamesModel)
class AssetsNamesModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    search_fields = (
        'es_name',
        'en_name'
    )

    list_display = (
        'es_name',
        'en_name',
        'created',
        'updated',
        'is_active',
    )

    list_display_links = (
        'es_name',
        'en_name'
    )

    readonly_fields = (
        'id',
        'created',
        'updated'
    )

    ordering = (
        'default_order',
        'created'
    )

    fieldsets = (
        (_('Details'), {
            'fields': (
                'id',
                'es_name',
                'en_name',
                'is_active',
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
        (
            _('Priority'), {
                'fields': (
                    'default_order',
                ),
                'classes': (
                    'collapse',
                )
            }
        )
    )


@admin.register(AssetCategoryModel)
class AssetCategoryModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = (
        'en_name',
        'es_name'
    )

    list_filter = (
        'is_active',
    )

    list_display = (
        'en_name',
        'es_name',
        'created',
        'updated',
        'is_active'
    )

    list_display_links = list_display[:2]

    ordering = (
        'default_order',
        '-created'
    )

    readonly_fields = (
        'id',
        'created',
        'updated',
    )

    fieldsets = (
        (_('Details'), {
            'fields': (
                'id',
                'es_name',
                'en_name',
                'description',
                'is_active',
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
        (
            _('Priority'), {
                'fields': (
                    'default_order',
                ),
                'classes': (
                    'collapse',
                )
            }
        )
    )


@admin.register(AssetModel)
class AssetModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    autocomplete_fields = (
        'asset_name',
        'category',
    )
    
    search_fields = (
        'id',
        'asset_name__es_name',
        'asset_name__en_name',

        'category__es_name',
        'category__en_name',
    )

    list_filter = (
        'is_active',
        QuantityTypeFilter,
        ZeroTotalQuantityFilter,
        HasImageFilter,
        'category',
    )

    list_display = (
        'get_asset_es_name',
        'get_asset_en_name',
        'category',
        'get_asset_total_quantity_by_type',
        'is_active',
    )

    list_display_links = list_display[:3]

    readonly_fields = (
        'id',
        'created',
        'updated',
        'get_asset_total_quantity_by_type',
    )

    ordering = (
        'default_order',
        'created'
    )

    fieldsets = (
        (_('Required Fields'), {
            'fields':
                (
                    'id',
                    'asset_img',
                    'asset_name',
                    'category',
                    'is_active',
                    'get_asset_total_quantity_by_type',
                )
        }
        ),
        (_('Optional Fields'), {
            'fields': (
                'observations',
                'description',
            ),
            'classes': (
                'collapse',
            )
        }
        ),
        (_('Dates'), {
            'fields': (
                'created',
                'updated'
            ),
            'classes': (
                'collapse',
            )
        }
        ),
        (
            _('Priority'), {
                'fields': (
                    'default_order',
                ),
                'classes': (
                    'collapse',
                )
            }
        )
    )

    def get_asset_es_name(self, obj):
        return obj.asset_name.es_name
    get_asset_es_name.short_description = _('Asset Name (ES)')

    def get_asset_en_name(self, obj):
        return obj.asset_name.en_name
    get_asset_en_name.short_description = _('Asset Name (EN)')

    def get_asset_total_quantity_by_type(self, obj):
        totals = obj.asset_total_quantity_by_type()
        return ", ".join(f"{key}: {value}" for key, value in totals.items())
    get_asset_total_quantity_by_type.short_description = _(
        'Total Quantity by Type')
