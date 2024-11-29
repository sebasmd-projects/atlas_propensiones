from django import forms
from django.utils.translation import gettext_lazy as _

from apps.project.specific.assets_management.assets.models import AssetModel

from .models import AssetCountryModel, AssetLocationModel, LocationModel


class AssetCountryForm(forms.ModelForm):
    country_name = forms.CharField(
        label=_('Country Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'asset_country_name',
                'type': 'text',
                'placeholder': _('Country Name'),
                'class': 'form-control',
                'aria-label': _('Country Name'),
                'aria-describedby': 'asset_country_name'
            }
        )
    )

    class Meta:
        model = AssetCountryModel
        exclude = [
            'created',
            'updated',
            'default_order',
            'is_active',
            'language'
        ]


class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['continent'].initial = LocationModel.ContinentChoices.SOUTH_AMERICA

    reference = forms.CharField(
        label=_('Reference'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'asset_location_reference',
                'type': 'text',
                'placeholder': _('Reference'),
                'class': 'form-control',
                'aria-label': _('Reference'),
                'aria-describedby': 'asset_location_reference'
            }
        )
    )

    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'asset_location_description',
                'placeholder': _('Description'),
                'class': 'form-control',
                'aria-label': _('Description'),
                'aria-describedby': 'asset_location_description'
            }
        )
    )

    continent = forms.ChoiceField(
        label=_('Continent'),
        required=True,
        choices=LocationModel.ContinentChoices.choices,
        widget=forms.Select(
            attrs={
                'id': 'asset_location_continent',
                'class': 'form-control',
                'aria-label': _('Continent'),
                'aria-describedby': 'asset_location_continent'
            }
        )
    )

    country = forms.ModelChoiceField(
        label=_('Country'),
        required=False,
        queryset=AssetCountryModel.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'asset_location_country',
                'class': 'form-control',
                'aria-label': _('Country'),
                'aria-describedby': 'asset_location_country'
            }
        )
    )

    class Meta:
        model = LocationModel
        exclude = [
            'created',
            'updated',
            'default_order',
            'is_active',
            'language'
        ]


class AssetLocationForm(forms.ModelForm):
    asset = forms.ModelChoiceField(
        label=_('Asset'),
        required=True,
        queryset=AssetModel.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'asset_location_asset',
                'class': 'form-control',
                'aria-label': _('Asset'),
                'aria-describedby': 'asset_location_asset'
            }
        )
    )

    location = forms.ModelChoiceField(
        label=_('Location'),
        required=True,
        queryset=LocationModel.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'asset_location_location',
                'class': 'form-control',
                'aria-label': _('Location'),
                'aria-describedby': 'asset_location_location'
            }
        )
    )

    amount = forms.IntegerField(
        label=_('Amount'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'id': 'asset_location_amount',
                'type': 'number',
                'placeholder': _('Amount'),
                'class': 'form-control',
                'aria-label': _('Amount'),
                'aria-describedby': 'asset_location_amount'
            }
        )
    )

    class Meta:
        model = AssetLocationModel
        exclude = [
            'created',
            'updated',
            'default_order',
            'is_active',
            'language'
        ]
