import uuid
from datetime import timedelta

from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from encrypted_model_fields.fields import (EncryptedCharField,
                                           EncryptedDateField,
                                           EncryptedEmailField)

from apps.common.utils.models import TimeStampedModel
from apps.project.common.users.signals import (firm_directory_path,
                                               passport_directory_path)


def validate_birth_date(value):
    today = timezone.now().date()
    min_date = today - timedelta(days=18*365)

    if value > today:
        raise ValidationError(
            _('The date of birth cannot be a future date.')
        )

    if value < min_date:
        raise ValidationError(
            _('User must be at least 18 years of age.')
        )
        
def default_birth_date():
    return timezone.now() - timedelta(days=18 * 365)

def default_date_of_expiry():
    return timezone.now() + timedelta(days=365)


class UserModel(TimeStampedModel, AbstractUser):
    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    first_name = models.CharField(
        _("first name"),
        max_length=150,
    )

    last_name = models.CharField(
        _("second name"),
        max_length=150,
        blank=True,
    )

    first_surname = models.CharField(
        _("first surname"),
        max_length=150,
    )

    second_surname = models.CharField(
        _("second surname"),
        max_length=150,
        blank=True,
    )

    email = EncryptedEmailField(
        _("email address"),
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'first_surname'
    ]

    def __str__(self) -> str:
        return f"{self.get_full_name()}"

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.first_surname = self.first_surname.title()
        self.second_surname = self.second_surname.title()
        self.username = self.username.lower()
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_project_common_users_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        unique_together = [['username', 'email']]


class CountryModel(TimeStampedModel):
    country_name = models.CharField(
        _('Country Name'),
        max_length=100,
        unique=True
    )

    country_code = models.CharField(
        _('Country Code'),
        max_length=5,
        unique=True
    )

    def __str__(self) -> str:
        return f"{self.country_name} ({self.country_code})"

    def save(self, *args, **kwargs):
        self.country_name = self.country_name.title()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_project_common_users_country'
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class StateModel(TimeStampedModel):
    state_name = models.CharField(
        _('State Name'),
        max_length=100,
    )

    country = models.ForeignKey(
        CountryModel,
        on_delete=models.CASCADE,
        related_name='states'
    )

    def __str__(self) -> str:
        return f"{self.state_name} {self.country.country_name}"

    def save(self, *args, **kwargs):
        self.state_name = self.state_name.title()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_project_common_users_state'
        unique_together = [['state_name', 'country']]
        verbose_name = _('State')
        verbose_name_plural = _('States')


class CityModel(TimeStampedModel):
    city_name = models.CharField(
        _('City Name'),
        max_length=100,
    )

    state = models.ForeignKey(
        StateModel,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    def __str__(self) -> str:
        return f"{self.city_name} {self.state.state_name}"

    def save(self, *args, **kwargs):
        self.city_name = self.city_name.title()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_project_common_users_city'
        unique_together = [['city_name', 'state']]
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class AddressModel(TimeStampedModel):
    country = models.ForeignKey(
        CountryModel,
        on_delete=models.SET_NULL,
        null=True
    )

    state = models.ForeignKey(
        StateModel,
        on_delete=models.SET_NULL,
        null=True
    )

    city = models.ForeignKey(
        CityModel,
        on_delete=models.SET_NULL,
        null=True
    )

    address_line_1 = EncryptedCharField(
        _('Address Line 1'),
        max_length=255
    )

    address_line_2 = EncryptedCharField(
        _('Address Line 2 (Optional)'),
        max_length=255,
        blank=True,
        null=True
    )

    postal_code = models.CharField(
        _('Postal Code'),
        max_length=10
    )

    passport_image = models.ImageField(
        _('Passport Image'),
        upload_to=passport_directory_path,
    )

    beneficiary_firm = models.ImageField(
        _('Beneficiary Firm'),
        upload_to=firm_directory_path,
    )

    def __str__(self) -> str:
        if self.address_line_2:
            return f"{self.country.country_name} {self.state.state_name} {self.city.city_name} {self.address_line_1} {self.address_line_2}"
        return f"{self.country.country_name} {self.state.state_name} {self.city.city_name} {self.address_line_1}"

    class Meta:
        db_table = 'apps_project_common_users_address'
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class UserPersonalInformationModel(TimeStampedModel):
    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='personal_information'
    )

    birth_date = EncryptedDateField(
        _('Birth Date'),
        validators=[validate_birth_date],
        default=default_birth_date,
    )

    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE
    )

    citizenship_country = EncryptedCharField(
        _('Citizenship'),
        max_length=100,
    )

    passport_id = EncryptedCharField(
        _('Passport Identification'),
        max_length=20,
    )

    date_of_issue = models.DateField(
        _('Date of Issue'),
        default=timezone.now
    )

    issuing_authority = models.CharField(
        _('Issuing Authority'),
        max_length=100,
    )

    date_of_expiry = models.DateField(
        _('Date of Expiry'),
        default=default_date_of_expiry
    )

    addresses = models.ManyToManyField(
        AddressModel,
        related_name='personal_information',
        blank=True,
    )

    phone_number_code = models.CharField(
        _('Phone Number Code'),
        max_length=5,
    )

    phone_number = EncryptedCharField(
        _('Phone Number'),
        max_length=25,
    )

    def __str__(self) -> str:
        return f"{self.user.get_full_name()}"

    def save(self, *args, **kwargs):
        self.issuing_authority = self.issuing_authority.title()
        super().save(*args, **kwargs)


auditlog.register(
    UserModel,
    serialize_data=True
)

auditlog.register(
    UserPersonalInformationModel,
    serialize_data=True
)
