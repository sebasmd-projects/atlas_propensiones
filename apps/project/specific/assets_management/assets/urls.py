from django.urls import path

from .views import AssetCategoryCreateView, AssetsCreateView

app_name = 'assets'

urlpatterns = [
    path(
        'asset/add/',
        AssetsCreateView.as_view(),
        name='create_asset'
    ),
    path(
        'asset/category/add/',
        AssetCategoryCreateView.as_view(),
        name='create_asset_category'
    ),
]
