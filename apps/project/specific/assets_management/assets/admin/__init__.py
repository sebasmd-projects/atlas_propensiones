
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from ..models import AssetCategoryModel, AssetModel
from .actions import update_total_quantities
from .filters import HasImageFilter, ZeroTotalQuantityFilter
from .forms import AssetModelForm
from .inlines import AssetLocationInline
from .resources import AssetModelResource


@admin.register(AssetModel)
class AssetModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    inlines = [AssetLocationInline]

    form = AssetModelForm

    actions = [update_total_quantities]

    def get_export_resource_class(self):
        return AssetModelResource

    search_fields = (
        'id',
        'name',
        'es_name',
        'category__name'
    )

    list_filter = (
        'is_active',
        'quantity_type',
        ZeroTotalQuantityFilter,
        HasImageFilter
    )

    list_display = (
        'es_name',
        'name',
        'category',
        'quantity_type',
        'total_quantity',
        'is_active',
    )

    list_display_links = list_display

    readonly_fields = (
        'created',
        'updated',
        'total_quantity',
    )

    ordering = (
        'default_order',
        'created'
    )

    fieldsets = (
        (_('Required Fields'), {'fields': (
            'asset_img',
            'name',
            'es_name',
            'category',
            'quantity_type',
            'total_quantity',
            'is_active',

        )}),
        (_('Optional Fields'), {'fields': (
            'observations',
            'default_order',
        )}),
        (_('Dates'), {'fields': (
            'created',
            'updated'
        )}),
    )


@admin.register(AssetCategoryModel)
class AssetCategoryModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['created', 'is_active']
    list_display = ['name', 'created']
    list_display_links = ['name']
    ordering = ['default_order', 'name', 'created']
    readonly_fields = ['created', 'updated']
