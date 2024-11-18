from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class KycConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.project.specific.documents.kyc'  
    verbose_name = _("KYC")
    verbose_name_plural = _("KYCs")
