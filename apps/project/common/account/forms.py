from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from apps.project.common.users.models import UserModel
from apps.project.common.users.validators import (UnicodeLastNameValidator,
                                                  UnicodeNameValidator,
                                                  UnicodeUsernameValidator)

from django.conf import settings

USER_TXT = _('User')
EMAIL_TXT = _('Email')
PASSWORD_TXT = _('Password')


class BaseUserForm(forms.ModelForm):
    username = forms.CharField(
        label=USER_TXT,
        validators=[UnicodeUsernameValidator()],
        required=True,
        widget=forms.TextInput(attrs={
            "id": "register_username",
            "type": "text",
            "placeholder": USER_TXT,
            "class": "form-control",
        })
    )
    email = forms.EmailField(
        label=EMAIL_TXT,
        required=True,
        widget=forms.EmailInput(attrs={
            "id": "register_email",
            "type": "email",
            "placeholder": EMAIL_TXT,
            "class": "form-control",
        })
    )
    password = forms.CharField(
        label=PASSWORD_TXT,
        required=True,
        widget=forms.PasswordInput(attrs={
            "id": "register_password",
            "type": "password",
            "placeholder": PASSWORD_TXT,
            "class": "form-control",
        })
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"),
        required=True,
        widget=forms.PasswordInput(attrs={
            "id": "register_confirm_password",
            "type": "password",
            "placeholder": _("Confirm Password"),
            "class": "form-control",
        })
    )
    first_name = forms.CharField(
        label=_("Names"),
        validators=[UnicodeNameValidator()],
        required=True,
        widget=forms.TextInput(attrs={
            "id": "register_first_name",
            "type": "text",
            "placeholder": _("Names"),
            "class": "form-control",
        })
    )
    last_name = forms.CharField(
        label=_("Last names"),
        validators=[UnicodeLastNameValidator()],
        required=True,
        widget=forms.TextInput(attrs={
            "id": "register_last_name",
            "type": "text",
            "placeholder": _("Last names"),
            "class": "form-control",
        })
    )

    unique_code = forms.CharField(
        label=_("Unique Code"),
        required=False,
        widget=forms.TextInput(
            attrs={
                "id": "register_unique_code",
                "type": "text",
                "placeholder": _("Unique Code"),
                "class": "form-control"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if cleaned_data['unique_code'] != settings.ATLAS_REGISTER_UNIQUE_CODE:
            self.add_error("unique_code", _("Invalid Unique Code"))
        
        if password and confirm_password:
            validate_password(password)
            if password != confirm_password:
                self.add_error("confirm_password", _("Passwords do not match"))
        return cleaned_data

    class Meta:
        model = UserModel
        fields = ("username", "email", "first_name", "last_name")


class AtlasUserRegisterForm(BaseUserForm):
    user_type = forms.ChoiceField(
        label=_("User Type"),
        required=True,
        choices=UserModel.UserTypeChoices.choices,
        widget=forms.Select(attrs={
            "id": "register_user_type",
            "class": "form-select",
        })
    )

    class Meta(BaseUserForm.Meta):
        fields = BaseUserForm.Meta.fields + ("user_type",)


class PropensionesUserRegisterForm(BaseUserForm):
    citizenship_number = forms.CharField(
        label=_("Citizenship Number"),
        required=False,
        widget=forms.TextInput(
            attrs={
                "id": "register_citizenship_number",
                "type": "text",
                "placeholder": _("Citizenship Number"),
                "class": "form-control",
            }
        )
    )

    class Meta(BaseUserForm.Meta):
        fields = BaseUserForm.Meta.fields + ("citizenship_number",)
