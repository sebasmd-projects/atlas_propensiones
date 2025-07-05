from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.utils.models import TimeStampedModel


class ProofOfLifeModel(TimeStampedModel):
    """
    Guarda la información necesaria para la verificación de prueba de vida (POL).
    """

    first_name = models.CharField(
        _("Primer nombre"),
        max_length=50
    )

    middle_name = models.CharField(
        _("Segundo nombre (opcional)"),
        max_length=50,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        _("Primer apellido"),
        max_length=50
    )

    second_last_name = models.CharField(
        _("Segundo apellido (opcional)"),
        max_length=50,
        blank=True,
        null=True
    )

    pol_confirmed = models.BooleanField(
        _("Confirmo la prueba de vida (Proof of life, POL)"),
        default=False
    )

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()

        if self.middle_name:
            self.middle_name = self.middle_name.upper()
        if self.second_last_name:
            self.second_last_name = self.second_last_name.upper()

        super().save(*args, **kwargs)

    class Meta:
        db_table = "apps_proof_of_life"
        verbose_name = _("Prueba de vida")
        verbose_name_plural = _("Pruebas de vida")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
