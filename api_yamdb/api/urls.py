from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.views import CommentViewSet, ReviewViewSet
from titles.views import CategoryViewSet, GenreViewSet, TitleViewSet
from users.views import APISignUp, APIToken, APIUser, UserViewSetForAdmin

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

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
