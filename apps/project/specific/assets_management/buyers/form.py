from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from .models import OfferModel


class CountryWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "es_country_name__icontains",
        "en_country_name__icontains",
    ]

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs['data-minimum-input-length'] = 2
        return attrs


class AssetNameWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "es_name__icontains",
        "en_name__icontains",
    ]

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs['data-minimum-input-length'] = 0
        return attrs


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
        ]
        widgets = {
            "buyer_country": CountryWidget,
            "asset": AssetNameWidget,
        }



class OfferUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].disabled = True
        self.fields['offer_type'].disabled = True

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
        ]
        widgets = {
            "buyer_country": CountryWidget,
        }
