from django.urls import path

from .views import (AtlasUserRegisterView, PropensionesUserRegisterView,
                    UserLogoutView, UserPreregisterView)

app_name = "account"

urlpatterns = [
    path(
        'account/register/',
        UserPreregisterView.as_view(),
        name='register'
    ),
    path(
        'account/register/atlas/',
        AtlasUserRegisterView.as_view(),
        name='register-atlas'
    ),
    path(
        'account/register/propensiones/',
        PropensionesUserRegisterView.as_view(),
        name='register-propensiones'
    ),
    path(
        'account/logout/',
        UserLogoutView.as_view(),
        name='logout'
    )
]
