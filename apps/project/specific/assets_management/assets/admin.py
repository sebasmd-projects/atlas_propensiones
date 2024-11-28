from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from .models import AssetCategoryModel


@admin.register(AssetCategoryModel)
class AssetCategoryModelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'es_name']
    list_filter = ['is_active']
    list_display = ['name', 'es_name', 'created', 'updated']
    list_display_links = ['name']
    ordering = ['default_order', 'name', 'created']
    readonly_fields = ['created', 'updated']