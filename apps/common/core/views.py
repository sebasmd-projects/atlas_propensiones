from django.views.generic.edit import FormView

from .forms import FormWithCaptcha


class IndexTemplateView(FormView):
    template_name = "pages/index/index.html"
    form_class = FormWithCaptcha
