from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.create.character.create import CreateCharacterView
from web.views.create.character.get_single import GetSingleCharacterView
from web.views.create.character.remove import RemoveCharacterView
from web.views.index import index
from web.views.user.accounts import get_user_info
from web.views.user.accounts.get_user_info import GetUserInfoView
from web.views.user.accounts.login import LoginView
from web.views.user.accounts.logout import LogoutView
from web.views.user.accounts.refresh_token import RefreshTokenView
from web.views.user.accounts.register import RegisterView
from web.views.user.profiles.update import UpdateProfileView

urlpatterns = [
    path('api/user/accounts/login/',LoginView.as_view()),
    path('api/user/accounts/logout/',LogoutView.as_view()),
    path('api/user/accounts/register/',RegisterView.as_view()),
    path("api/user/accounts/refresh_token/",RefreshTokenView.as_view()),
    path("api/user/accounts/get_user_info/",GetUserInfoView.as_view()),
    path("api/user/profiles/update/",UpdateProfileView.as_view()),
    path("api/create/character/create/",CreateCharacterView.as_view()),
    path("api/create/character/update/",UpdateProfileView.as_view()),
    path("api/create/character/remove/",RemoveCharacterView.as_view()),
    path("api/create/character/get_single/",GetSingleCharacterView.as_view()),
    path('', index),

    re_path(r'^(?!media/|static/|assets/).*$', index),
]
