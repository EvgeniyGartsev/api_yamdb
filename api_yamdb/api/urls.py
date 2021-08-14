from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reviews.views import CommentViewSet, ReviewViewSet
from titles.views import CategoryViewSet, GenreViewSet, TitleViewSet
from users.views import APISignUp, APIToken, UserViewSetForAdmin, APIUser

"""Импорты для второго варианта вьюсетов комментариев и отзывов."""
# from .views import CommentReadCreateViewSet, CommentPatchDeleteViewSet,\
# ReviewReadCreateViewSet, ReviewPatchDeleteViewSet


router = DefaultRouter()
router.register(r'reviews/(?P<review_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'reviews', ReviewViewSet, basename='reviews')

"""Роутеры для второго варианта вьюсетов комментариев и отзывов."""

# router.register(r'reviews/(?P<review_id>\d+)/comments',
#                 CommentReadCreateViewSet, basename='comments')
# router.register(r'reviews/(?P<review_id>\d+)/comments',
#                 CommentPatchDeleteViewSet, basename='edit-comments')
# router.register(r'reviews', ReviewReadCreateViewSet,
#                 basename='reviews')
# router.register(r'reviews',  ReviewPatchDeleteViewSet,
#                 basename='reviews-edit')

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSetForAdmin, basename='users')

urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view(), name='signup'),
    path('v1/auth/token/', APIToken.as_view(), name='token'),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router.urls)),
]
