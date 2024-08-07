from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user-create"),
    path("list/", UserListAPIView.as_view(), name="user-list"),
    path("retrieve/", UserRetrieveAPIView.as_view(), name="user-retrieve"),
    path("update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("destroy/", UserDestroyAPIView.as_view(), name="user-destroy"),
    path("obtain/", TokenObtainPairView.as_view(), name="obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
]
