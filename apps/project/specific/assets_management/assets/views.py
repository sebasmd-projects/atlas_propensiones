from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import AssetCategoryForm, AssetModelForm


# Asset views
class AssetsCreateView(LoginRequiredMixin, FormView):
    template_name = 'assets/create.html'
    form_class = AssetModelForm


class AssetsListView(LoginRequiredMixin, ListView):
    template_name = 'assets/list.html'


class AssetDetailView(LoginRequiredMixin, DetailView):
    template_name = 'assets/datail.html'


# Category views
class AssetCategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assets/category/create.html'
    form_class = AssetCategoryForm


class AssetCategoryListView(LoginRequiredMixin, ListView):
    template_name = 'assets/category/list.html'


class AssetCategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'assets/category/detail.html'
