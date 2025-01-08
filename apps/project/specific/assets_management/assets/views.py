from django.views.generic import TemplateView

from apps.project.specific.assets_management.assets_location.models import (
    AssetLocationModel, LocationModel)
from apps.project.specific.assets_management.assets_location.views import \
    HolderRequiredMixin
from apps.project.specific.assets_management.buyers.models import OfferModel


class HolderTemplateview(HolderRequiredMixin, TemplateView):
    template_name = 'dashboard/pages/assets_management/assets/holders/holder_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assets = AssetLocationModel.objects.filter(
            asset__is_active=True,
            is_active=True,
            created_by=self.request.user
        )

        pre_assets = None

        locations = LocationModel.objects.filter(
            is_active=True,
            created_by=self.request.user
        )

        offers = OfferModel.objects.filter(
            is_active=True,
            is_approved=True,
        )

        context['assets'] = assets
        context['locations'] = locations
        context['offers'] = offers if assets else None
        # pre_assets
        context['total_offers'] = offers.count()

        return context
