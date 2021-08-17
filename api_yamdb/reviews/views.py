from api.permissions import IsAuthorOrAdministratorOrReadOnly
from api.serializers import CommentSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from titles.models import Title

from reviews.models import Comment, Review


class CommentViewSet(viewsets.ModelViewSet):
    """POST для всех авторизованных, PATCH для модеров, админов и автора."""
    permission_classes = (IsAuthorOrAdministratorOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def create(self, request, *args, **kwargs):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user, review_id=review.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))
        if self.request.user != comment.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    """POST для всех авторизованных, PATCH для модеров, админов и автора."""
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrAdministratorOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = Title.objects.get(id=title_id)
        return title.reviews.all()

    def create(self, request, *args, **kwargs):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        serializer = ReviewSerializer(data=request.data)
        # Один отзыв на произведение для одного человека
        if title.reviews.filter(author=self.request.user).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save(author=self.request.user, title_id=title.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        if self.request.user != review.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
