from django.db.models import Count
from rest_framework import generics, permissions
from poems_drf_api.permissions import IsOwnerOrReadOnly
from .models import Poem
from .serializers import PoemSerializer


class PoemList(generics.ListCreateAPIView):
    """
    List poems or create a poem if logged in.
    """
    serializer_class = PoemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.annotate(
        likes_count=Count('like', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'like_created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poem, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PoemSerializer
    queryset = Poem.objects.annotate(
        likes_count=Count('like', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
