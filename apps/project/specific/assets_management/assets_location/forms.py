from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms

from .models import AssetLocationModel, LocationModel


class CountryWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "es_country_name__icontains",
        "en_country_name__icontains",
    ]
    
    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs['data-minimum-input-length'] = 0
        return attrs

class LocationModelForm(forms.ModelForm):

    class Meta:
        model = LocationModel
        fields = ['reference', 'description', 'country']
        widgets = {
            "country": CountryWidget,
        }


class AssetLocationModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['location'].queryset = LocationModel.objects.filter(created_by=user)
    
    class Meta:
        model = AssetLocationModel
        fields = ['asset', 'location', 'quantity_type', 'amount']
        
class AssetUpdateLocationModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['location'].queryset = LocationModel.objects.filter(created_by=user)
        self.fields['asset'].disabled = True
        
    class Meta:
        model = AssetLocationModel
        fields = ['asset', 'location', 'quantity_type', 'amount']