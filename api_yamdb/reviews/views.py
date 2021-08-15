"""Добавить миксины, если первый вариант вьюсетов не работает."""
from api.permissions import IsAuthorOrStaffOrReadOnly
from api.serializers import CommentSerializer, ReviewSerializer
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response
from titles.models import Title

from reviews.models import Review

"""Первый варитант вьюсетов."""


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = Review.objects.get(id=review_id)
        return review.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [IsAuthorOrStaffOrReadOnly]
        return super().get_permissions()


class ReviewViewSet(viewsets.ModelViewSet):

    serializer_class = ReviewSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = Title.objects.get(id=title_id)
        return title.reviews

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [IsAuthorOrStaffOrReadOnly]
        return super().get_permissions()


"""Второй вариант вьюсетов."""

# class CommentReadCreateViewSet(mixins.ListModelMixin,
#                                mixins.CreateModelMixin,
#                                viewsets.GenericViewSet):
#     serializer_class = (CommentSerializer,)
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#         return Response(serializer.data)
#
#     def get_queryset(self):
#         review_id = self.kwargs.get('review_id')
#         review = Review.objects.get(id=review_id)
#         return review.comments
#
#
# class CommentPatchDeleteViewSet(mixins.UpdateModelMixin,
#                                 mixins.DestroyModelMixin,
#                                 viewsets.GenericViewSet):
#
#     serializer_class = (CommentSerializer,)
#     permission_classes = (IsAuthorOrStaffOrReadOnly,)
#
#     def get_queryset(self):
#         review_id = self.kwargs.get('review_id')
#         review = Review.objects.get(id=review_id)
#         return review.comments
#
#
# class ReviewReadCreateViewSet(mixins.ListModelMixin,
#                               mixins.CreateModelMixin,
#                               viewsets.GenericViewSet):
#
#     serializer_class = ReviewSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         title_id = self.kwargs.get('title_id')
#         title = Title.objects.get(id=title_id)
#         return title.comments
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#         return Response(serializer.data)
#
#
# class ReviewPatchDeleteViewSet(mixins.UpdateModelMixin,
#                                mixins.DestroyModelMixin,
#                                viewsets.GenericViewSet):
#
#     serializer_class = (ReviewSerializer,)
#     permission_classes = (IsAuthorOrStaffOrReadOnly,)
#
#     def get_queryset(self):
#         title_id = self.kwargs.get('title_id')
#         title = Title.objects.get(id=title_id)
#         return title.comments
