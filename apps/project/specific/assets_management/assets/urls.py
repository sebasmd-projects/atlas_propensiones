from django.urls import path

from .views import (AssetCategoryCreateView, AssetCategoryDetailView,
                    AssetCategoryListView, AssetDetailView, AssetUpdateView, AssetsCreateView,
                    AssetsListView, HolderTemplateview, AssetDeleteView)

app_name = 'assets'

urlpatterns = [
    path(
        'asset/holder/',
        HolderTemplateview.as_view(),
        name='holder_index'
    ),
    path(
        'asset/edit/<int:pk>/',
        AssetUpdateView.as_view(),
        name='edit_asset'
    ),
    path(
        'asset/delete/<int:pk>/',
        AssetDeleteView.as_view(),
        name='delete_asset'
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
