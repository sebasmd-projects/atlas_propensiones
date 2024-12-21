from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import get_language
from django.views.generic import CreateView, DetailView

from apps.project.common.users.models import UserModel

from .form import OfferForm
from .models import OfferModel


class BuyerRequiredMixin(LoginRequiredMixin):
    """Mixin to check if the user has the 'buyer' category.

    Args:
        LoginRequiredMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Mixin to check if the user has the 'buyer' category.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        allowed_user_types = [
            UserModel.UserTypeChoices.BUYER,
        ]

        if (
            not hasattr(request.user, 'user_type') or
            request.user.user_type not in allowed_user_types and
            not request.user.is_superuser and
            not request.user.is_staff
        ):
            return redirect(reverse('core:index'))

        return super().dispatch(request, *args, **kwargs)


class BuyerCreateView(BuyerRequiredMixin, CreateView):
    model = OfferModel
    template_name = 'dashboard/pages/assets_management/assets/buyers/buyer_dashboard.html'
    context_object_name = 'offers'
    form_class = OfferForm

    def get_queryset(self):
        return OfferModel.objects.filter(created_by=self.request.user)


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
