from django.urls import path

from .views import AssetsTemplateView

app_name = 'assets'

urlpatterns = [
    path('assets/', AssetsTemplateView.as_view(), name='register'),
]
