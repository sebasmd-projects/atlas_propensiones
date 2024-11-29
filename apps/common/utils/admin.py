from django.contrib import admin

from .models import IPBlockedModel, RequestLogModel

admin.site.register(IPBlockedModel)

admin.site.register(RequestLogModel)
