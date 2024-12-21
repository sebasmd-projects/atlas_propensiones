from django import forms
from .models import OfferModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = [
            'asset',
            'offer_type',
            'quantity_type',
            'offer_amount',
            'offer_quantity',
            'en_observation',
            'es_observation',
            'en_description',
            'es_description',
            'buyer_country',
            'es_procedure',
            'en_procedure'
        ]
