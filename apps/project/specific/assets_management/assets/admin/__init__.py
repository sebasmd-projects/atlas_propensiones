
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
        'category__name',
        'created_by__username',
        'created_by__first_name',
        'created_by__last_name',
        'created_by__email',
    )

    list_filter = (
        'is_active',
        'quantity_type',
        ZeroTotalQuantityFilter,
        HasImageFilter
    )

    list_display = (
        'created_by',
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
        (_('Required Fields'), {
            'fields':
                (
                    'created_by',
                    'asset_img',
                    'name',
                    'es_name',
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

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
        
@admin.register(AssetCategoryModel)
class AssetCategoryModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = [
        'name',
        'es_name'
    ]

    list_filter = [
        'is_active'
    ]

    list_display = [
        'name',
        'es_name',
        'created',
        'is_active'
    ]

    list_display_links = [
        'name',
        'es_name'
    ]

    ordering = [
        'default_order',
        'name',
        'es_name',
        'created'
    ]

    readonly_fields = [
        'created',
        'updated',
    ]