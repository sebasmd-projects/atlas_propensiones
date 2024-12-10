from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AssetModel


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
