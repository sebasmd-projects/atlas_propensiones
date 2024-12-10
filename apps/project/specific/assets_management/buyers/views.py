from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.views.generic.detail import DetailView

from .models import OfferModel


class OfferDetailView(DetailView):
    model = OfferModel
    template_name = 'dashboard/pages/assets_management/offers/offer_detail.html'
    context_object_name = 'offer'

    def get_object(self, queryset=None):
        """Fetch the OfferModel instance by the ID provided in the URL."""
        return get_object_or_404(OfferModel, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        """Add custom context data to be used in the template."""
        context = super().get_context_data(**kwargs)
        offer = context['offer']

        # Obtener el idioma actual del usuario
        current_language = get_language()

        # Obtener el banner y el texto (procedimiento) de acuerdo con el idioma
        banner = offer.es_banner.url if current_language == 'es' and offer.es_banner else offer.en_banner.url if offer.en_banner else None
        procedure = offer.es_procedure if current_language == 'es' else offer.en_procedure

        # Si no hay banner, mostramos el procedimiento como texto
        context['banner'] = banner
        context['procedure'] = procedure

        return context
