from django.contrib.auth import logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView

from apps.project.common.users.models import UserModel

from .forms import AtlasUserRegisterForm, PropensionesUserRegisterForm


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'two_factor:login'
            )
        )


class AtlasUserRegisterView(FormView):
    template_name = "dashboard/account/atlas_register.html"
    form_class = AtlasUserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            UserModel.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                user_type=form.cleaned_data['user_type']
            )
        except IntegrityError as e:
            if "email_hash" in str(e):
                form.add_error(
                    "email",
                    _("A user with this email already exists.")
                )
                return self.form_invalid(form)
            raise e

        return super(AtlasUserRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(AtlasUserRegisterView, self).form_invalid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('two_factor:login')


class PropensionesUserRegisterView(FormView):
    template_name = "dashboard/account/propensiones_register.html"
    form_class = PropensionesUserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        UserModel.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            citizenship_number=form.cleaned_data['citizenship_number']
        )
        return super(PropensionesUserRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(PropensionesUserRegisterView, self).form_invalid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('two_factor:login')


class UserPreregisterView(TemplateView):
    template_name = "dashboard/account/pre_register.html"
