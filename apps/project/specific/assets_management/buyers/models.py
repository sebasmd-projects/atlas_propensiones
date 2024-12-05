import logging
import os
from datetime import date

from auditlog.registry import auditlog
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.core.functions import generate_md5_hash
from apps.common.utils.models import TimeStampedModel
from apps.project.specific.assets_management.assets.models import \
    AssetCategoryModel
from apps.project.specific.assets_management.assets_location.models import \
    AssetCountryModel

logger = logging.getLogger(__name__)
UserModel = get_user_model()


class OfferModel(TimeStampedModel):
    class QuantityTypeChoices(models.TextChoices):
        OTHER = "O", _("Other")
        UNITS = "U", _("Units")
        BOXES = "B", _("Boxes")
        CONTAINERS = "C", _("Containers")

    def offers_directory_path(instance, filename) -> str:
        """
        Generate a file path for an offer image.
        Path format: offer/{slugified_name}/img/YYYY/MM/DD/{hashed_filename}.{extension}
        """
        try:
            es_name = slugify(instance.asset_es)[:40]
            base_filename, file_extension = os.path.splitext(filename)
            filename_hash = generate_md5_hash(base_filename)
            path = os.path.join(
                "offer", es_name, "img",
                str(date.today().year),
                str(date.today().month),
                str(date.today().day),
                f"{filename_hash[:10]}{file_extension}"
            )
            return path
        except Exception as e:
            logger.error(
                f"Error generating file path for {filename}: {e}"
            )
            raise e

    class OfferTypeChoices(models.TextChoices):
        SOVEREIGN = "S", _("Sovereign Purchase")
        PRIVATE = "P", _("Private Purchase (Sovereign)")
        BUSINESS = "B", _("Business Purchase")
        GOVERNMENT = "G", _("Government Purchase")

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name="offers_offers_user",
        verbose_name=_("Created By"),
        null=True
    )

    asset_es = models.CharField(
        _("Asset (ES)"),
        max_length=255,
    )

    asset_en = models.CharField(
        _("Asset (EN)"),
        max_length=255,
        blank=True,
        null=True
    )

    asset_type = models.ForeignKey(
        AssetCategoryModel,
        on_delete=models.CASCADE,
        related_name="buyers_offer_assetcategory",
        verbose_name=_("category"),
        null=True
    )

    offer_type = models.CharField(
        _("Offer Type"),
        max_length=255,
        choices=OfferTypeChoices.choices,
        default=OfferTypeChoices.PRIVATE
    )

    quantity_type = models.CharField(
        _("quantity type"),
        max_length=255,
        choices=QuantityTypeChoices.choices,
        default=QuantityTypeChoices.BOXES
    )

    offer_amount = models.DecimalField(
        _("Offer Amount per quantity type in USD"),
        max_digits=20,
        decimal_places=1,
        default=0
    )

    offer_quantity = models.PositiveIntegerField(
        _("Quantity needed"),
        default=0
    )

    buyer_country = models.ForeignKey(
        AssetCountryModel,
        on_delete=models.CASCADE,
        related_name="buyers_offer_country",
        verbose_name=_("Country"),
        null=True
    )

    procedure = CKEditor5Field(
        _('Procedure'),
        config_name='default'
    )

    banner = models.ImageField(
        _("Banner"),
        upload_to=offers_directory_path,
        null=True,
        blank=True
    )

    def total_value(self):
        return self.offer_amount * self.offer_quantity

    def __str__(self) -> str:
        return f"{self.asset_type} - {self.asset_es} - {self.asset_en} - {self.buyer_country} - {self.offer_quantity}"

    class Meta:
        db_table = "apps_buyers_offer"
        verbose_name = _("1. Offer")
        verbose_name_plural = _("1. Offers")
        ordering = ["default_order", "-created"]


auditlog.register(OfferModel, serialize_data=True)
