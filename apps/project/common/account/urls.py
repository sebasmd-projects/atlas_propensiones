from django.urls import path

from .views import UserLogoutView, UserRegisterView

app_name = "account"

urlpatterns = [
    path(
        'account/register/',
        UserRegisterView.as_view(),
        name='register'
    ),
    path(
        'account/logout/',
        UserLogoutView.as_view(),
        name='logout'
    )
]
