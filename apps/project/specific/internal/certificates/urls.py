from django.urls import path

from .views import CertificateInputView, CertificateDetailView, LockoutTimeView

app_name = 'certificates'

urlpatterns = [
    path('certificate/', CertificateInputView.as_view(), name='input'),
    path('certificate/<uuid:pk>/', CertificateDetailView.as_view(), name='detail'),
    path('lockout-time/', LockoutTimeView.as_view(), name='lockout_time'),
]
