from django import forms
from django.utils.translation import gettext_lazy as _

from .models import AssetCategoryModel, AssetModel


class AssetModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = AssetCategoryModel.objects.filter(
            is_active=True
        )
        self.fields['category'].empty_label = None
        self.fields['quantity_type'].empty_label = None
        self.fields['quantity_type'].initial = AssetModel.QuantityTypeChoices.BOXES

    es_name = forms.CharField(
        label=_('Name (ES)'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'asset_es_name',
                'type': 'text',
                'placeholder': _('Asset Name (ES)'),
                'class': 'form-control',
                'aria-label': _('Asset Name (ES)'),
                'aria-describedby': 'asset_es_name'
            }
        )
    )

    name = forms.CharField(
        label=_('Name (EN)'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'asset_name',
                'type': 'text',
                'placeholder': _('Asset Name (EN)'),
                'class': 'form-control',
                'aria-label': _('Asset Name (EN)'),
                'aria-describedby': 'asset_name'
            }
        )
    )

    asset_img = forms.ImageField(
        label=_('Image'),
        required=False,
        widget=forms.FileInput(
            attrs={
                'id': 'asset_img',
                'type': 'file',
                'class': 'form-control',
                'aria-label': _('Image'),
                'aria-describedby': 'asset_img'
            }
        )
    )

    category = forms.ModelChoiceField(
        label=_('Category'),
        required=True,
        queryset=AssetCategoryModel.objects.all(),
        widget=forms.Select(
            attrs={
                'id': 'asset_category',
                'class': 'form-control',
                'aria-label': _('Category'),
                'aria-describedby': 'asset_category'
            }
        )
    )

    quantity_type = forms.ChoiceField(
        label=_('Quantity Type'),
        required=True,
        choices=AssetModel.QuantityTypeChoices.choices,
        widget=forms.Select(
            attrs={
                'id': 'asset_quantity_type',
                'class': 'form-control',
                'aria-label': _('Quantity Type'),
                'aria-describedby': 'asset_quantity_type'
            }
        )
    )

    observations = forms.CharField(
        label=_('Observations'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'asset_observations',
                'placeholder': _('Observations'),
                'class': 'form-control',
                'aria-label': _('Observations'),
                'aria-describedby': 'asset_observations',
                'rows': 3
            }
        )
    )

    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'asset_description',
                'placeholder': _('Description'),
                'class': 'form-control',
                'aria-label': _('Description'),
                'aria-describedby': 'asset_description',
                'rows': 3
            }
        )
    )

    class Meta:
        model = AssetModel
        exclude = [
            'created',
            'updated',
            'created_by',
            'total_quantity',
            'default_order',
            'is_active',
            'language'
        ]


class AssetCategoryForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Category Name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category_name',
                'type': 'text',
                'placeholder': _('Category Name'),
                'class': 'form-control',
                'aria-label': _('Category Name'),
                'aria-describedby': 'category_name'
            }
        )
    )

    es_name = forms.CharField(
        label=_('Category Name (ES)'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category_es_name',
                'type': 'text',
                'placeholder': _('Category Name (ES)'),
                'class': 'form-control',
                'aria-label': _('Category Name (ES)'),
                'aria-describedby': 'category_es_name'
            }
        )
    )

    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'category_description',
                'placeholder': _('Description'),
                'class': 'form-control',
                'aria-label': _('Description'),
                'aria-describedby': 'category_description'
            }
        )
    )

    class Meta:
        model = AssetCategoryModel
        exclude = [
            'created',
            'updated',
            'default_order',
            'is_active',
            'language'
        ]
