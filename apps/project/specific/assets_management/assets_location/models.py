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


class AssetCountryModel(TimeStampedModel):
    country_name = models.CharField(
        _('Country Name'),
        max_length=100,
        unique=True
    )

    def __str__(self) -> str:
        return f"{self.country_name} ({self.country_code})"

    def save(self, *args, **kwargs):
        self.country_name = self.country_name.title()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'apps_assets_location_country'
        verbose_name = _('3. Country')
        verbose_name_plural = _('3. Countries')


class LocationModel(TimeStampedModel):
    """Represents a physical location, including reference, description, and continent."""

    class ContinentChoices(models.TextChoices):
        """Enumeration of continent choices."""
        AFRICA = "AF", _("Africa")
        ANTARCTICA = "AN", _("Antarctica")
        ASIA = "AS", _("Asia")
        CENTRAL_AMERICA = "CA", _("Central America")
        EUROPE = "EU", _("Europe")
        NORTH_AMERICA = "NA", _("North America")
        OCEANIA = "OC", _("Oceania")
        SOUTH_AMERICA = "SA", _("South America")

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name="assetslocation_location_user",
        verbose_name=_("Created By"),
        null=True
    )

    reference = models.CharField(
        _("reference"),
        max_length=150
    )

    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )

    continent = models.CharField(
        _("continent"),
        max_length=3,
        choices=ContinentChoices.choices,
        default=ContinentChoices.EUROPE
    )

    country = models.ForeignKey(
        AssetCountryModel,
        on_delete=models.CASCADE,
        related_name="assetlocation_location_country",
        verbose_name=_("Country")
    )

    def __str__(self) -> str:
        """Returns a string representation of the location."""
        message = f"{self.reference} - {self.get_continent_display()}"
        return message

    class Meta:
        db_table = "apps_assets_location_location"
        verbose_name = _("2. Location")
        verbose_name_plural = _("2. Locations")
        ordering = ["default_order", "reference", "-created"]


class AssetLocationModel(TimeStampedModel):
    """Represents the relationship between an Asset and a Location, including the quantity of assets at that location."""

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
        verbose_name=_("Assets")
    )

    location = models.ForeignKey(
        LocationModel,
        on_delete=models.CASCADE,
        related_name="assetlocation_assetlocation_location",
        verbose_name=_("location"),
    )

    amount = models.PositiveBigIntegerField(
        _("amount")
    )

    def __str__(self) -> str:
        return f"{self.location.reference} - {self.amount} - {self.asset.es_name}"

    class Meta:
        db_table = "apps_assets_location_assetlocation"
        verbose_name = _("1. Location Registration")
        verbose_name_plural = _("1. Locations Registration")
        ordering = ["default_order", "asset", "-created"]


# Signal connections
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

# Register models with audit log
auditlog.register(LocationModel, serialize_data=True)
auditlog.register(AssetLocationModel, serialize_data=True)
