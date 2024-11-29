from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import AssetCountryForm, AssetLocationForm, LocationForm
from .models import AssetCountryModel, AssetLocationModel, LocationModel

"""
    AssetCountry Views
    
"""


class AssetCountryCreateView(LoginRequiredMixin, FormView):
    template_name = 'assets/locations/country/create.html'
    form_class = AssetCountryForm


class AssetCountryListView(LoginRequiredMixin, ListView):
    template_name = 'assets/locations/country/list.html'
    model = AssetCountryModel


"""

    Location Views

"""


class LocationCreateView(LoginRequiredMixin, FormView):
    template_name = 'assets/locations/location/create.html'
    form_class = LocationForm


class LocationListView(LoginRequiredMixin, ListView):
    template_name = 'assets/locations/location/list.html'
    model = LocationModel


class LocationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'assets/locations/location/detail.html'
    model = LocationModel


"""
    AssetLocation Views

"""


class AssetLocationCreateView(LoginRequiredMixin, FormView):
    template_name = 'assets/locations/asset_location/create.html'
    form_class = AssetLocationForm


class AssetLocationListView(LoginRequiredMixin, ListView):
    template_name = 'assets/locations/asset_location/list.html'
    model = AssetLocationModel


class AssetLocationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'assets/locations/asset_location/detail.html'
    model = AssetLocationModel
