
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from ..models import AssetCategoryModel, AssetModel, AssetsNamesModel
from .actions import update_total_quantities
from .filters import HasImageFilter, ZeroTotalQuantityFilter
from .forms import AssetModelForm
from .inlines import AssetLocationInline
from .resources import (AssetCategoryResource, AssetModelResource,
                        AssetsNamesResource)


@admin.register(AssetsNamesModel)
class AssetsNamesModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = AssetsNamesResource

    search_fields = (
        'es_name',
        'en_name'
    )

    list_display = (
        'es_name',
        'en_name',
        'created',
        'updated'
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
                'en_name'
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
    )


@admin.register(AssetCategoryModel)
class AssetCategoryModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = AssetCategoryResource

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
                'is_active'
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
    )


@admin.register(AssetModel)
class AssetModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AssetModelResource
    
    inlines = (
        AssetLocationInline,
    )

    form = AssetModelForm

    actions = [update_total_quantities]

    def get_export_resource_class(self):
        return AssetModelResource

    search_fields = (
        'id',
        'asset_name__es_name',
        'asset_name__en_name',

        'category__es_name',
        'category__en_name',

        'created_by__username',
        'created_by__first_name',
        'created_by__last_name',
        'created_by__email',

        'total_quantity'
    )

    list_filter = (
        'is_active',
        'quantity_type',
        ZeroTotalQuantityFilter,
        HasImageFilter,
        'category',
    )

    list_display = (
        'created_by',
        'get_asset_es_name',
        'get_asset_en_name',
        'category',
        'quantity_type',
        'total_quantity',
        'is_active',
    )

    list_display_links = list_display[:3]

    readonly_fields = (
        'id',
        'created',
        'updated',
        'total_quantity',
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
                    'created_by',
                    'asset_img',
                    'asset_name',
                    'category',
                    'quantity_type',
                    'total_quantity',
                    'is_active',
                )
        }
        ),
        (_('Optional Fields'), {
            'fields': (
                'observations',
                'description',
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
