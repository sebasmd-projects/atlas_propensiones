from django.urls import path
from . import views  # Asegúrate de tener al menos una vista
app_name= 'kyc'
urlpatterns = [
    path('', views.index, name='index'),  # Esta es una URL de ejemplo
]
