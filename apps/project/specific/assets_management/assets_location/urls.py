from django.urls import path

from .views import (
    AssetCountryCreateView, AssetCountryListView,
    AssetLocationCreateView, AssetLocationDetailView,
    AssetLocationListView, LocationCreateView,
    LocationDetailView, LocationListView
)

app_name = 'assets_location'

urlpatterns = [
    path(
        'asset/locations/country/add/',
        AssetCountryCreateView.as_view(),
        name='create_country'
    ),
    path(
        'asset/locations/country/list/',
        AssetCountryListView.as_view(),
        name='list_country'
    ),
    path(
        'asset/locations/add/',
        LocationCreateView.as_view(),
        name='create_location'
    ),
    path(
        'asset/locations/list/',
        LocationListView.as_view(),
        name='list_location'
    ),
    path(
        'asset/locations/detail/<int:pk>/',
        LocationDetailView.as_view(),
        name='detail_location'
    ),
    path(
        'asset/locations/location/add/',
        AssetLocationCreateView.as_view(),
        name='create_asset_location'
    ),
    path(
        'asset/locations/location/list/',
        AssetLocationListView.as_view(),
        name='list_asset_location'
    ),
    path(
        'asset/locations/location/detail/<int:pk>/',
        AssetLocationDetailView.as_view(),
        name='detail_asset_location'
    ),
]
