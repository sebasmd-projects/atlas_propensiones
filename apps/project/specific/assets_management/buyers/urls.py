from django.urls import path

from apps.project.specific.assets_management.buyers.views import \
    OfferDetailView

app_name = "buyers"

urlpatterns = [
    path(
        'offers/<uuid:id>/detail/',
        OfferDetailView.as_view(),
        name='offer_details'
    ),
]
