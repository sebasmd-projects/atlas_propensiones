import logging
import os
import uuid
from datetime import date

from auditlog.registry import auditlog
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.core.functions import generate_md5_hash
from apps.common.utils.models import TimeStampedModel
from apps.project.specific.assets_management.assets.signals import (
    auto_delete_asset_img_on_change, auto_delete_asset_img_on_delete)

logger = logging.getLogger(__name__)
UserModel = get_user_model()


class AssetCategoryModel(TimeStampedModel):
    es_name = models.CharField(
        _("category (ES)"),
        max_length=50,
    )

    en_name = models.CharField(
        _("category (EN)"),
        max_length=50,
        blank=True,
        null=True
    )

    description = models.TextField(
        _("description"),
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.es_name

    def save(self, *args, **kwargs):
        self.es_name = self.es_name.title().strip()
        if self.en_name:
            self.en_name = self.en_name.title().strip()
        super(AssetCategoryModel, self).save(*args, **kwargs)

    class Meta:
        db_table = "apps_assets_assetcategory"
        verbose_name = _("2. Category")
        verbose_name_plural = _("2. Categories")
        ordering = ["default_order", "-created"]


class AssetsNamesModel(TimeStampedModel):
    es_name = models.CharField(
        _("asset (es)"),
        max_length=255,
    )

    en_name = models.CharField(
        _("asset (en)"),
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.es_name

    def save(self, *args, **kwargs):
        self.es_name = self.es_name.title().strip()
        if self.en_name:
            self.en_name = self.en_name.title().strip()
        super(AssetsNamesModel, self).save(*args, **kwargs)

    class Meta:
        db_table = "apps_assets_assetsnames"
        verbose_name = _("3. Asset Name")
        verbose_name_plural = _("3. Asset Names")
        ordering = ["default_order", "-created"]


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
            es_name = slugify(instance.asset_name.es_name)[:40]
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
        related_name="assets_assets_user",
        verbose_name=_("Created By"),
        null=True
    )

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

    asset_name = models.ForeignKey(
        AssetsNamesModel,
        on_delete=models.CASCADE,
        related_name="assets_asset_assetsnames",
        verbose_name=_("asset")
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
        expected_total = self.assetlocation_assetlocation_asset.aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        return expected_total

    def __str__(self) -> str:
        return f"{self.asset_name.es_name} - {self.get_quantity_type_display()} - {self.total_quantity}"

    class Meta:
        db_table = "apps_assets_asset"
        verbose_name = _("1. Asset")
        verbose_name_plural = _("1. Assets")
        ordering = ["default_order", "-created"]


post_delete.connect(
    auto_delete_asset_img_on_delete,
    sender=AssetModel
)

pre_save.connect(
    auto_delete_asset_img_on_change,
    sender=AssetModel
)

auditlog.register(
    AssetCategoryModel,
    serialize_data=True
)

auditlog.register(
    AssetsNamesModel,
    serialize_data=True
)

auditlog.register(
    AssetModel,
    serialize_data=True
)
