from django.urls import path

from apps.project.specific.assets_management.buyers.views import (
    BuyerCreateView, OfferDetailView)

app_name = "buyers"

urlpatterns = [
    path(
        'offers/<uuid:id>/detail/',
        OfferDetailView.as_view(),
        name='offer_details'
    ),
    path(
        'asset/buyer/',
        BuyerCreateView.as_view(),
        name='buyer_index'
    ),
]
