from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView)

from apps.project.common.users.models import UserModel
from apps.project.specific.assets_management.assets_location.models import \
    AssetLocationModel
from apps.project.specific.assets_management.buyers.models import OfferModel

from .forms import AssetCategoryForm, AssetModelForm
from .models import AssetCategoryModel, AssetModel


class HolderRequiredMixin:
    """
    Mixin to check if the user has the 'holder' category.
    """

    def dispatch(self, request, *args, **kwargs):
        # Check if the user has allowed roles or is a superuser/staff
        allowed_user_types = [
            UserModel.UserTypeChoices.HOLDER,
            UserModel.UserTypeChoices.REPRESENTATIVE,
            UserModel.UserTypeChoices.INTERMEDIARY
        ]
        if (request.user.user_type not in allowed_user_types and
                not request.user.is_superuser and
                not request.user.is_staff):
            return redirect(reverse('core:index'))

        return super().dispatch(request, *args, **kwargs)


class HolderTemplateview(LoginRequiredMixin, HolderRequiredMixin, TemplateView):
    template_name = 'dashboard/pages/assets_management/assets/holders/holder_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['assets'] = AssetModel.objects.filter(
        #     created_by=self.request.user
        # )

        context['offers'] = OfferModel.objects.filter(
            is_active=True,
        )
        
        context['assets'] = AssetModel.objects.filter(
            created_by=self.request.user
        ).annotate(
            country_quantities=Sum(
                F('assetlocation_assetlocation_asset__amount')
            )
        )

        return context


class AssetUpdateView(LoginRequiredMixin, HolderRequiredMixin, UpdateView):
    model = AssetModel
    form_class = AssetModelForm
    template_name = 'dashboard/pages/assets_management/assets/holders/partials/edit_asset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = AssetCategoryModel.objects.filter(
            is_active=True)
        context['quantity_type_choices'] = AssetModel.QuantityTypeChoices.choices
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': True})
        return response

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('assets:holder_index')


class AssetDeleteView(DeleteView):
    model = AssetModel
    template_name = None
    success_url = reverse_lazy('assets:holder_index')

    def form_valid(self, form):
        self.object = self.get_object()
        user = self.request.user
        if user == self.object.created_by or user.is_staff or user.is_superuser:
            if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                self.object.delete()
                return JsonResponse({'success': True})
            return super().form_valid(form)
        else:
            return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)



# Asset views
class AssetsCreateView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/pages/assets_management/assets/create.html'
    form_class = AssetModelForm


class AssetDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/pages/assets_management/assets/datail.html'


# Category views
class AssetCategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/pages/assets_management/assets/category/create.html'
    form_class = AssetCategoryForm


class AssetCategoryListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/pages/assets_management/assets/category/list.html'


class AssetCategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/pages/assets_management/assets/category/detail.html'
