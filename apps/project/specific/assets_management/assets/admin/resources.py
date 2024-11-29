from import_export import resources

from ..models import AssetModel


class AssetModelResource(resources.ModelResource):
    def dehydrate_quantity_type(self, asset):
        return asset.get_quantity_type_display()

    class Meta:
        model = AssetModel
