from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.project.common.users.validators import (UnicodeLastNameValidator,
                                                  UnicodeNameValidator,
                                                  UnicodeUsernameValidator)

UserModel = get_user_model()
USER_OR_EMAIL_TXT = _('User or Email')
PASSWORD_TXT = _('Password')
USER_TXT = _('User')
EMAIL_TXT = _('Email')


class UserRegisterForm(forms.ModelForm):
    username_validator = UnicodeUsernameValidator()
    name_validator = UnicodeNameValidator()
    last_name_validator = UnicodeLastNameValidator()

    username = forms.CharField(
        label=USER_TXT,
        validators=[username_validator],
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "register_username",
                "type": "text",
                "placeholder": USER_TXT,
                "class": "form-control",
                'aria-label': USER_TXT,
                'aria-describedby': 'register_username'
            }
        )
    )

    email = forms.CharField(
        label=EMAIL_TXT,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "id": "register_email",
                "type": "email",
                "placeholder": EMAIL_TXT,
                "class": "form-control",
                'aria-label': EMAIL_TXT,
                'aria-describedby': 'register_email'
            }
        )
    )

    password = forms.CharField(
        label=PASSWORD_TXT,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id": "register_password",
                'type': 'password',
                'placeholder': PASSWORD_TXT,
                'class': 'form-control',
                'aria-label': PASSWORD_TXT,
                'aria-describedby': 'register_password'
            }
        )
    )

    confirm_password = forms.CharField(
        label=_('Confirm Password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id": "register_confirm_password",
                "type": "password",
                "placeholder": _('Confirm Password'),
                "class": "form-control",
                'aria-label': _('Confirm Password'),
                'aria-describedby': 'register_confirm_password'
            }
        )
    )

    first_name = forms.CharField(
        label=_("Names"),
        required=True,
        validators=[name_validator],
        widget=forms.TextInput(
            attrs={
                "id": "register_first_name",
                "type": "text",
                "placeholder": _("Names"),
                "class": "form-control",
                'aria-label': _('Names'),
                'aria-describedby': 'register_first_name'
            }
        )
    )

    last_name = forms.CharField(
        label=_("Last names"),
        required=True,
        validators=[last_name_validator],
        widget=forms.TextInput(
            attrs={
                "id": "register_last_name",
                "type": "text",
                "placeholder": _("Last names"),
                "class": "form-control",
                'aria-label': _('Last names'),
                'aria-describedby': 'register_last_name'
            }
        )
    )

    user_type = forms.ChoiceField(
        label=_('User Type'),
        required=True,
        choices=UserModel.UserTypeChoices.choices,
        widget=forms.Select(
            attrs={
                "id": "register_user_type",
                "class": "form-select",
                'aria-label': _('User Type'),
                'aria-describedby': 'register_user_type'
            }
        )
    )

    def clean_confirm_password(self):
        validate_password(
            self.cleaned_data["password"],
        )

        validate_password(
            self.cleaned_data["confirm_password"],
        )

        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            raise ValidationError(_('Passwords do not match'))
    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "user_type"
        )


class UserUpdateProfile(forms.ModelForm):
    pass
