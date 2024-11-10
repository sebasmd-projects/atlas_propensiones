import base64
import random
import string
from datetime import datetime
from io import BytesIO

import barcode
from barcode.writer import ImageWriter
from django.http import JsonResponse
from django.views.generic import FormView, ListView

from .forms import BarcodeForm
from .models import BarcodeRegistrationModel


def generate_random_code(length=4):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_barcode(text):
    buffer = BytesIO()
    barcode_class = barcode.get_barcode_class('code128')
    barcode_image = barcode_class(text, writer=ImageWriter())
    barcode_image.write(buffer)
    buffer.seek(0)
    return buffer


class BarcodeGeneratorView(FormView):
    template_name = "barcode_form.html"
    form_class = BarcodeForm

    def form_valid(self, form):
        # Obtener datos del formulario
        reference: str = form.cleaned_data['reference']
        description = form.cleaned_data['description']
        custom_text: str = form.cleaned_data['custom_text_input'].strip()
        include_nit = form.cleaned_data['include_nit']
        include_date = form.cleaned_data['include_date']
        include_random_code = form.cleaned_data['include_random_code']

        # Construir el texto del código de barras
        barcode_text = custom_text
        components = [custom_text]

        if include_nit:
            components.insert(0, '901.409.813-7')

        if include_date:
            components.append(datetime.now().strftime("%d%m%Y"))

        if include_random_code:
            components.append(generate_random_code())

        barcode_text = ' '.join(components).strip()

        # Generar el código de barras
        buffer = generate_barcode(barcode_text)
        barcode_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Guardar en el modelo
        existing_record = BarcodeRegistrationModel.objects.filter(
            reference=reference.upper(),
            description=description,
            code_information=barcode_text
        ).first()

        if not existing_record:
            BarcodeRegistrationModel.objects.create(
                reference=reference.upper(),
                description=description,
                custom_text_input=custom_text,
                code_information=barcode_text
            )

        return JsonResponse(
            {
                "barcode_image": f"data:image/png;base64,{barcode_base64}"
            }
        )
