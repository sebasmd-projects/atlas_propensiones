from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, DetailView, FormView, ListView,
    TemplateView
)

from .forms import AssetCategoryForm, AssetModelForm
from .models import AssetModel


class HolderTemplateview(TemplateView):
    template_name = 'dashboard/pages/assets_management/assets/holders/holder_dashboard.html'


# Asset views
class AssetsCreateView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/pages/assets_management/assets/create.html'
    form_class = AssetModelForm


class AssetsListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/pages/assets_management/assets/list.html'
    queryset = AssetModel.objects.all()


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
