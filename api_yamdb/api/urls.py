from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reviews.views import CommentViewSet, ReviewViewSet
from titles.views import CategoryViewSet, GenreViewSet, TitleViewSet

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

urlpatterns = [
    path('v1/', include(router.urls)),
]
