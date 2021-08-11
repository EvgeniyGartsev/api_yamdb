from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from titles.views import CategoryViewSet, GenreViewSet, TitleViewSet
from users.views import APISignUp, APIToken, UserViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view()),
    path('v1/auth/token/', APIToken.as_view()),
    path('v1/', include(router.urls)),
]
