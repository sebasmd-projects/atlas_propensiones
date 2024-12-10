import random
import string
import uuid

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_delete, pre_save
from django.utils.translation import gettext_lazy as _

from apps.common.utils.models import TimeStampedModel
from apps.project.specific.assets_management.assets.models import AssetModel

from .signals import (update_asset_total_quantity_on_location,
                      update_asset_total_quantity_on_location_change,
                      update_asset_total_quantity_on_location_delete,
                      update_asset_total_quantity_on_location_is_active_change)

UserModel = get_user_model()


def generate_random_code(length=4):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


class AssetCountryModel(TimeStampedModel):
    class ContinentChoices(models.TextChoices):
        AFRICA = "AF", _("Africa")
        ANTARCTICA = "AN", _("Antarctica")
        ASIA = "AS", _("Asia")
        CENTRAL_AMERICA = "CA", _("Central America")
        EUROPE = "EU", _("Europe")
        NORTH_AMERICA = "NA", _("North America")
        OCEANIA = "OC", _("Oceania")
        SOUTH_AMERICA = "SA", _("South America")

    continent = models.CharField(
        _("continent"),
        max_length=3,
        choices=ContinentChoices.choices,
        default=ContinentChoices.SOUTH_AMERICA
    )

    es_country_name = models.CharField(
        _('Country Name (ES)'),
        max_length=100,
    )

    en_country_name = models.CharField(
        _('Country Name (EN)'),
        max_length=100,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.get_continent_display()} - {self.es_country_name} - {self.en_country_name}"

    def save(self, *args, **kwargs):
        self.es_country_name = self.es_country_name.title().strip()
        self.en_country_name = self.en_country_name.title().strip()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_assets_location_country'
        unique_together = ['continent', 'es_country_name', 'en_country_name']
        verbose_name = _('3. Country')
        verbose_name_plural = _('3. Countries')
        ordering = ["default_order", "-created", 'continent']


class LocationModel(TimeStampedModel):
    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name="assetslocation_location_user",
        verbose_name=_("Created By"),
        null=True
    )

    reference = models.CharField(
        _("location reference"),
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )

    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )

    country = models.ForeignKey(
        AssetCountryModel,
        on_delete=models.CASCADE,
        related_name="assetlocation_location_country",
        verbose_name=_("Country")
    )

    def __str__(self):
        return "{} ({})".format(self.reference, self.country.es_country_name)

    def save(self, *args, **kwargs):
        if self.reference:
            self.reference = self.reference.upper().strip()

        if not self.reference:
            self.reference = "{} - {}".format(
                self.country.country_name,
                generate_random_code()
            ).upper()

        super(LocationModel, self).save(*args, **kwargs)

    class Meta:
        db_table = "apps_assets_location_location"
        unique_together = ['reference', 'country']
        verbose_name = _("2. Location")
        verbose_name_plural = _("2. Locations")
        ordering = ["default_order", "-created"]


class AssetLocationModel(TimeStampedModel):
    class QuantityTypeChoices(models.TextChoices):
        UNITS = "U", _("Units")
        BOXES = "B", _("Boxes")
        CONTAINERS = "C", _("Containers")

    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name="assetslocation_assetslocation_user",
        verbose_name=_("Created By"),
        null=True
    )

    asset = models.ForeignKey(
        AssetModel,
        on_delete=models.CASCADE,
        related_name="assetlocation_assetlocation_asset",
        verbose_name=_("Asset")
    )

    location = models.ForeignKey(
        LocationModel,
        on_delete=models.CASCADE,
        related_name="assetlocation_assetlocation_location",
        verbose_name=_("location"),
    )

    quantity_type = models.CharField(
        _("quantity type"),
        max_length=255,
        choices=QuantityTypeChoices.choices,
        default=QuantityTypeChoices.BOXES
    )

    amount = models.PositiveBigIntegerField(
        _("amount")
    )

    def __str__(self) -> str:
        return "{} - {} - {} - {} - {}".format(
            self.asset.asset_name.es_name,
            self.get_quantity_type_display(),
            self.amount,
            self.location.reference,
            self.created_by.email,
        )

    class Meta:
        db_table = "apps_assets_location_assetlocation"
        verbose_name = _("1. Location Registration")
        verbose_name_plural = _("1. Locations Registration")
        ordering = ["default_order", "-created"]


post_save.connect(
    update_asset_total_quantity_on_location,
    sender=AssetLocationModel
)

pre_delete.connect(
    update_asset_total_quantity_on_location_delete,
    sender=AssetLocationModel
)

pre_save.connect(
    update_asset_total_quantity_on_location_change,
    sender=AssetLocationModel
)

pre_save.connect(
    update_asset_total_quantity_on_location_is_active_change,
    sender=AssetLocationModel
)

auditlog.register(
    LocationModel,
    serialize_data=True
)

auditlog.register(
    AssetLocationModel,
    serialize_data=True
)
