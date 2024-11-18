from django.shortcuts import render

# Create your views here.
# apps/project/specific/documents/kyc/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de inicio de KYC")
