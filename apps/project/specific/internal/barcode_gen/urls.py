from django.urls import path

from .views import BarcodeGeneratorView

app_name = "barcode_gen"

urlpatterns = [
    path(
        "barcode/generate/",
        BarcodeGeneratorView.as_view(),
        name="barcode_generate"
    ),
]
