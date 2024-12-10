from django.contrib import admin

from .models import CodeRegistrationModel
from import_export.admin import ImportExportActionModelAdmin

@admin.register(CodeRegistrationModel)
class CodeRegistrationModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'reference',
        'custom_text_input',
        'code_information',
        'created',
        'updated'
    )

    search_fields = (
        'reference',
        'custom_text_input',
        'code_information'
    )

    list_filter = (
        'is_active',
    )

    readonly_fields = (
        'created',
        'updated'
    )

    ordering = (
        '-default_order',
    )

    fieldsets = (
        (
            'Barcode Information',
            {
                'fields': (
                    'reference',
                    'custom_text_input',
                    'code_information',
                )
            }
        ),
        (
            'Status',
            {
                'fields': (
                    'is_active',
                )
            }
        ),
        (
            'System Information',
            {
                'fields': (
                    'created',
                    'updated',
                )
            }
        )
    )
