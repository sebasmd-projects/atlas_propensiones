from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Abstract model providing timestamp fields (created and updated) and additional metadata.

    Args:
        models.Model (class): Base Django model class.
    """
    history = AuditlogHistoryField()

    language_choices = [
        ('es', _('Spanish')),
        ('en', _('English')),
    ]

    language = models.CharField(
        _("language"),
        max_length=4,
        choices=language_choices,
        default='es',
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _('created'),
        default=timezone.now,
        editable=False
    )

    updated = models.DateTimeField(
        _('updated'),
        auto_now=True,
        editable=False
    )

    is_active = models.BooleanField(
        _("is active"),
        default=True
    )

    default_order = models.PositiveIntegerField(
        _('priority'),
        default=1,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
        ordering = ['default_order']


class IPBlockedModel(TimeStampedModel):
    class ReasonsChoices(models.TextChoices):
        SERVER_HTTP_REQUEST = 'RA', _('Attempts to obtain forbidden urls')
        SECURITY_KEY_ATTEMPTS = 'SK', _(
            'Multiple failed security key entry attempts'
        )

    is_active = models.BooleanField(_("is blocked"), default=True)
    current_ip = models.CharField(_('current user IP'), max_length=150)
    reason = models.CharField(
        _("reason"), max_length=4, choices=ReasonsChoices.choices, default=ReasonsChoices.SERVER_HTTP_REQUEST)
    blocked_until = models.DateTimeField(
        _("blocked until"), null=True, blank=True)
    session_info = models.JSONField(
        _("session information"), default=dict, blank=True)

    def __str__(self):
        return f"{self.current_ip} - Blocked until {self.blocked_until}"

    class Meta:
        db_table = 'apps_common_utils_ipblocked'
        verbose_name = 'Blocked IP'
        verbose_name_plural = 'Blocked IPs'


class WhiteListedIPModel(TimeStampedModel):
    current_ip = models.CharField(
        _('current user IP'),
        max_length=150
    )

    reason = models.CharField(
        _("reason"),
        max_length=150,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.current_ip}"

    class Meta:
        db_table = 'apps_utils_whitelistedip'
        verbose_name = 'WhiteListed IP'
        verbose_name_plural = 'WhiteListed IPs'


class RequestLogModel(TimeStampedModel):
    """A model to log requests."""
    requests = models.JSONField(
        _("requests"),
        blank=True,
        null=True,
        default=dict
    )

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of RequestLogModel."""
        instance, _ = cls.objects.get_or_create(id=1)
        return instance

    def add_request_entry(self, entry):
        """Add a request entry to the log.

        :param entry: The request entry to add.
        :type entry: dict
        """
        requests = self.requests or []
        requests.insert(0, entry)
        self.requests = requests
        self.save()

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = f'apps_utils_requestlog'
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')


auditlog.register(
    IPBlockedModel,
    serialize_data=True
)

auditlog.register(
    WhiteListedIPModel,
    serialize_data=True
)
