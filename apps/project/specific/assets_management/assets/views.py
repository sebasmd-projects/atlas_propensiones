from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import (CreateView, DetailView, FormView, ListView,
                                  TemplateView)

from apps.project.specific.assets_management.buyers.models import OfferModel

from .forms import AssetCategoryForm, AssetModelForm
from .models import AssetModel


class HolderRequiredMixin:
    """
    Mixin to check if the user has the 'holder' category.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.user_type == 'H':
            return redirect(reverse('core:index'))
        return super().dispatch(request, *args, **kwargs)


class HolderTemplateview(LoginRequiredMixin, HolderRequiredMixin, TemplateView):
    template_name = 'dashboard/pages/assets_management/assets/holders/holder_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add assets and postures to the context
        context['assets'] = AssetModel.objects.filter(created_by=self.request.user)
        context['offers'] = OfferModel.objects.all()
        return context

class AssetsListView(LoginRequiredMixin, HolderRequiredMixin, ListView):
    template_name = 'dashboard/pages/assets_management/assets/list.html'
    model = AssetModel
    context_object_name = 'assets'
    
    def get_queryset(self):
        return AssetModel.objects.filter(created_by=self.request.user)


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
