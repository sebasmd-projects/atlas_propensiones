from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.project.common.users.models import UserModel
from apps.project.specific.assets_management.assets_location.forms import (
    AssetLocationModelForm, AssetUpdateLocationModelForm, LocationModelForm)
from apps.project.specific.assets_management.assets_location.models import \
    AssetLocationModel

from .models import AssetLocationModel, LocationModel


class HolderRequiredMixin(LoginRequiredMixin):
    """
    Mixin to check if the user has the 'holder' category.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        # Define los tipos de usuario permitidos
        allowed_user_types = [
            UserModel.UserTypeChoices.HOLDER,
            UserModel.UserTypeChoices.REPRESENTATIVE,
            UserModel.UserTypeChoices.INTERMEDIARY
        ]

        # Comprueba si el usuario tiene el tipo permitido o es superuser/staff
        if (
            not hasattr(request.user, 'user_type') or
            request.user.user_type not in allowed_user_types and
            not request.user.is_superuser and
            not request.user.is_staff
        ):
            return redirect(reverse('core:index'))

        return super().dispatch(request, *args, **kwargs)


class LocationCreateView(HolderRequiredMixin, CreateView):
    model = LocationModel
    form_class = LocationModelForm
    template_name = 'dashboard/pages/assets_management/location/add_location.html'
    success_url = reverse_lazy('assets_location:add_asset_location')

    def get_queryset(self):
        return LocationModel.objects.filter(created_by=self.request.user)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetLocationCreateView(HolderRequiredMixin, CreateView):
    model = AssetLocationModel
    form_class = AssetLocationModelForm
    template_name = 'dashboard/pages/assets_management/asset_location/add_asset_location.html'
    success_url = reverse_lazy('assets:holder_index')

    def get_queryset(self):
        return AssetLocationModel.objects.filter(created_by=self.request.user)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AssetUpdateView(HolderRequiredMixin, UpdateView):
    model = AssetLocationModel
    form_class = AssetUpdateLocationModelForm
    template_name = 'dashboard/pages/assets_management/asset_location/edit_asset_location.html'
    success_url = reverse_lazy('assets:holder_index')

    def get_queryset(self):
        return AssetLocationModel.objects.filter(created_by=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
