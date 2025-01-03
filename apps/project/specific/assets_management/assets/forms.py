from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AssetModel, PreRegistrationAssetModel


class AssetModelForm(forms.ModelForm):
    class Meta:
        model = AssetModel
        fields = [
            'asset_img',
            'asset_name',
            'category',
            'description',
            'observations',
        ]


class PreRegistrationAssetForm(forms.ModelForm):

    class Meta:
        model = PreRegistrationAssetModel
        fields = ['has_item', 'es_observations', 'en_observations']
        widgets = {
            'has_item': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_observations': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observaciones'}),
            'en_observations': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observations'}),
        }