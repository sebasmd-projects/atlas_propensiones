import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.utils.models import TimeStampedModel


class ContactModel(TimeStampedModel):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    name = models.CharField(
        _('name'),
        max_length=255
    )

    last_name = models.CharField(
        _('last name'),
        max_length=255
    )

    email = models.EmailField(
        _('email'),
        max_length=255,
    )

    subject = models.CharField(
        _('subject'),
        max_length=255
    )

    message = models.TextField(
        _('message'),
    )

    class Meta:
        db_table = 'apps_common_core_contact'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.name
