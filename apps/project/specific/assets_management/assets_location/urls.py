from django.urls import path

from .views import AssetLocationCreateView, LocationCreateView, AssetUpdateView

app_name = 'assets_location'

urlpatterns = [
    path(
        'asset/add/location/',
        LocationCreateView.as_view(),
        name='add_location'
    ),
    path(
        'asset/add/',
        AssetLocationCreateView.as_view(),
        name='add_asset_location'
    ),
    path(
        'asset/update/<uuid:pk>/',
        AssetUpdateView.as_view(),
        name='update_asset_location'
    )
]
