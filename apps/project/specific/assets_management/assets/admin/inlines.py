from django.contrib import admin

from apps.project.specific.assets_management.assets_location.models import \
    AssetLocationModel


class AssetLocationInline(admin.TabularInline):
    model = AssetLocationModel
    extra = 1
    min_num = 0
    fk_name = 'asset'
    exclude = ('language', 'default_order')
