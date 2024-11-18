from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import LegalAdvisorModel

class LegalAdvisorAdmin(admin.ModelAdmin):
    list_display = (
        'legal_advisor_first_name',
        'legal_advisor_last_name',
        'legal_advisor_email',
        'legal_advisor_country',
        'detail_link',  # Asegúrate de que esto esté en list_display
        'created',
        'updated'
    )

admin.site.register(LegalAdvisorModel, LegalAdvisorAdmin)
