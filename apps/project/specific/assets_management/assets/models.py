import logging
import os
from datetime import date

from auditlog.registry import auditlog
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.core.functions import generate_md5_hash
from apps.common.utils.models import TimeStampedModel
from apps.project.specific.assets_management.assets.signals import (
    auto_delete_asset_img_on_change, auto_delete_asset_img_on_delete)

logger = logging.getLogger(__name__)


class AssetCategoryModel(TimeStampedModel):
    name = models.CharField(
        _("category (EN)"),
        max_length=50,
    )

    es_name = models.CharField(
        _("category (ES)"),
        max_length=50,
    )

    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.es_name

    class Meta:
        db_table = "apps_assets_assetcategory"
        verbose_name = _("Asset Category")
        verbose_name_plural = _("Asset Categories")
        ordering = ["default_order", "es_name", "-created"]


class AssetModel(TimeStampedModel):
    class QuantityTypeChoices(models.TextChoices):
        OTHER = "O", _("Other")
        UNITS = "U", _("Units")
        BOXES = "B", _("Boxes")
        CONTAINERS = "C", _("Containers")

    def assets_directory_path(instance, filename) -> str:
        """
        Generate a file path for an asset image.
        Path format: asset/{slugified_name}/img/YYYY/MM/DD/{hashed_filename}.{extension}
        """
        try:
            es_name = slugify(instance.es_name)[:40]
            base_filename, file_extension = os.path.splitext(filename)
            filename_hash = generate_md5_hash(base_filename)
            path = os.path.join(
                "asset", es_name, "img",
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

    asset_img = models.ImageField(
        _("img"),
        max_length=255,
        upload_to=assets_directory_path,
        blank=True,
        null=True
    )

    observations = models.TextField(
        _("observations"),
        default="",
        blank=True,
        null=True
    )

    name = models.CharField(
        _("english name"),
        max_length=255
    )

    es_name = models.CharField(
        _("spanish name"),
        max_length=255,
    )

    category = models.ForeignKey(
        AssetCategoryModel,
        on_delete=models.CASCADE,
        related_name="assets_asset_assetcategory",
        verbose_name=_("category")
    )

    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )

    quantity_type = models.CharField(
        _("quantity type"),
        max_length=255,
        choices=QuantityTypeChoices.choices,
        default=QuantityTypeChoices.BOXES
    )

    total_quantity = models.BigIntegerField(
        _("total lump sum"),
        default=0
    )

    def asset_total_quantity(self):
        # total quantity matches the sum of all related asset locations.
        expected_total = self.assetlocation_asset.aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        return expected_total

    def __str__(self) -> str:
        return f"{self.es_name} - {self.get_quantity_type_display()} - {self.total_quantity}"

    class Meta:
        db_table = "apps_assets_asset"
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")
        unique_together = [['name', 'quantity_type']]
        ordering = ["default_order", "es_name", "-created"]


post_delete.connect(auto_delete_asset_img_on_delete, sender=AssetModel)
pre_save.connect(auto_delete_asset_img_on_change, sender=AssetModel)

# Register the model with audit log for tracking changes
auditlog.register(AssetModel, serialize_data=True)
