from django.urls import path

from .views import (AssetCategoryCreateView, AssetCategoryDetailView,
                    AssetCategoryListView, AssetDetailView, AssetsCreateView,
                    AssetsListView, HolderTemplateview)

app_name = 'assets'

urlpatterns = [
    path(
        'asset/holder/',
        HolderTemplateview.as_view(),
        name='holder_index'
    ),
    path(
        'asset/add/',
        AssetsCreateView.as_view(),
        name='create_asset'
    ),
    path(
        'asset/list/',
        AssetsListView.as_view(),
        name='list_assets'
    ),
    path(
        'asset/detail/',
        AssetDetailView.as_view(),
        name='detail_asset'
    ),
    path(
        'asset/category/add/',
        AssetCategoryCreateView.as_view(),
        name='create_asset_category'
    ),
    path(
        'asset/category/list/',
        AssetCategoryListView.as_view(),
        name='list_asset_categories'
    ),
    path(
        'asset/category/detail/',
        AssetCategoryDetailView.as_view(),
        name='detail_asset_category'
    ),
]
