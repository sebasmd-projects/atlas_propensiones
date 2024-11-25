

import hashlib
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from encrypted_model_fields.fields import EncryptedCharField

from apps.common.utils.models import TimeStampedModel
from apps.project.common.users.models import UserModel


class CertificateModel(TimeStampedModel):
    class DocumentTypeChoices(models.TextChoices):
        CC = 'CC', _('Citizen ID (CC)')
        CE = 'CE', _('Foreigner ID (CE)')
        PPT = 'PPT', _('Special Residence Permit (PPT)')
        TI = 'TI', _('Identity Card (TI)')
        PA = 'PA', _('Passport (PA)')
        RC = 'RC', _('Civil Registry (RC)')
        NIT = 'NIT', _('Tax Identification Number (NIT)')
        RUT = 'RUT', _('Single Tax Registry (RUT)')
        CD = 'CD', _('Diplomatic ID Card (CD)')

    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        verbose_name=_('User'),
        related_name='certificates',
        blank=True,
        null=True
    )

    name = models.CharField(
        _('Names'),
        max_length=100
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=100,
        default=''
    )

    document_type = models.CharField(
        _('Document type'),
        max_length=4,
        choices=DocumentTypeChoices.choices,
        default=DocumentTypeChoices.CC
    )

    document_number = EncryptedCharField(
        _('Document number'),
        max_length=20,
    )

    document_number_hash = models.CharField(
        max_length=64,
        editable=False,
        default='',
    )

    approved = models.BooleanField(
        _('Approved'),
        default=True,
    )
    
    approved_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        verbose_name=_('Approved by'),
        related_name='approved_certificates',
        blank=True,
        null=True
    )
    
    approval_date = models.DateField(
        _('Approval date'),
        blank=True,
        null=True
    )

    def masked_document_number(self):
        """Returns the ID number with all but the last four digits masked."""
        document_number_str = str(self.document_number)
        last_four = document_number_str[-4:]
        masked = '*' * (len(document_number_str) - 4) + last_four
        return masked

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.last_name = self.last_name.upper()
        self.document_number_hash = hashlib.sha256(
            self.document_number.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {self.masked_document_number()}'

    class Meta:
        db_table = "apps_project_specific_documents_certificates_certificate"
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        ordering = ["default_order", "-created"]
        unique_together = ['document_number', 'document_type']
        permissions = [
            ('view_certificate', 'Can view certificate list'),
        ]
