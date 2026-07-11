from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.index import index
from web.views.user.accounts.login import LoginView
from web.views.user.accounts.logout import LogoutView
from web.views.user.accounts.register import RegisterView

urlpatterns = [
    path('api/user/accounts/login/',LoginView.as_view()),
    path('api/user/accounts/logout/',LogoutView.as_view()),
    path('api/user/accounts/register/',RegisterView.as_view()),
    path("api/user/accounts/refresh_token/",TokenRefreshView.as_view()),
    path('', index)
]
