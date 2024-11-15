from django import forms
from django.utils.translation import gettext_lazy as _

from .models import BarcodeRegistrationModel


class BarcodeForm(forms.ModelForm):
    include_nit = forms.BooleanField(
        label=_("Include NIT"),
        required=False
    )

    include_date = forms.BooleanField(
        label=_("Include Date (DDMMYYYY)"),
        required=False
    )

    include_random_code = forms.BooleanField(
        label=_("Include Random Code (4 digits)"),
        required=False
    )
    
    generate_qr_code = forms.BooleanField(
        label=_("Generate QR Code"),
        required=False
    )

    class Meta:
        model = BarcodeRegistrationModel
        fields = [
            'reference',
            'description',
            'custom_text_input'
        ]
        widgets = {
            'reference': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Reference'),
                    'required': True
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Description')
                }
            ),
            'custom_text_input': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Custom Text'),
                    'required': True
                }
            )
        }
