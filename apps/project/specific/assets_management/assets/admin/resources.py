from import_export import fields, resources
from import_export.resources import ModelResource

from ..models import AssetCategoryModel, AssetModel, AssetsNamesModel


class AssetCategoryResource(ModelResource):
    id = fields.Field(
        attribute='id',
        column_name='ID'
    )

    es_name = fields.Field(
        attribute='es_name',
        column_name='Category (ES)'
    )

    en_name = fields.Field(
        attribute='en_name',
        column_name='Category (EN)'
    )

    def dehydrate_es_name(self, obj):
        return obj.es_name.title()

    def dehydrate_en_name(self, obj):
        return obj.en_name.title() if obj.en_name else ''

    class Meta:
        model = AssetCategoryModel
        fields = (
            'id',
            'es_name',
            'en_name',
            'created',
            'updated'
        )


class AssetsNamesResource(ModelResource):
    id = fields.Field(
        attribute='id',
        column_name='ID'
    )

    es_name = fields.Field(
        attribute='es_name',
        column_name='Asset (ES)'
    )

    en_name = fields.Field(
        attribute='en_name',
        column_name='Asset (EN)'
    )

    def dehydrate_es_name(self, obj):
        return obj.es_name.title()

    def dehydrate_en_name(self, obj):
        return obj.en_name.title() if obj.en_name else ''

    class Meta:
        model = AssetsNamesModel
        fields = (
            'id',
            'es_name',
            'en_name',
            'created',
            'updated'
        )


class AssetModelResource(ModelResource):
    id = fields.Field(attribute='id', column_name='ID')
    asset_name_es = fields.Field(column_name='Asset (ES)')
    asset_name_en = fields.Field(column_name='Asset (EN)')
    category_es = fields.Field(column_name='Category (ES)')
    category_en = fields.Field(column_name='Category (EN)')

    def dehydrate_asset_name_es(self, obj):
        return obj.asset_name.es_name

    def dehydrate_asset_name_en(self, obj):
        return obj.asset_name.en_name if obj.asset_name.en_name else ''

    def dehydrate_category_es(self, obj):
        return obj.category.es_name

    def dehydrate_category_en(self, obj):
        return obj.category.en_name if obj.category.en_name else ''

    def dehydrate_quantity_type(self, obj):
        return obj.get_quantity_type_display()

    def dehydrate_created_by(self, obj):
        return f"{obj.created_by.get_full_name()} ({obj.created_by.username})" if obj.created_by else "N/A"

    class Meta:
        model = AssetModel
        fields = (
            'id',
            'asset_name_es',
            'asset_name_en',
            'category_es',
            'category_en',
            'quantity_type',
            'total_quantity',
            'created',
            'updated',
            'created_by'
        )
