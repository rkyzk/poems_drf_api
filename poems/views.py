from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poem
from .serializers import PoemSerializer
from poems_drf_api.permissions import IsOwnerOrReadOnly


class PoemList(APIView):
    serializer_class = PoemSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        poems = Poem.objects.all()
        serializer = PoemSerializer(
            poems, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PoemSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PoemDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PoemSerializer

    def get_object(self, pk):
        """handle the case in which poem with the given id doesn't exit."""
        try:
            poem = Poem.objects.get(pk=pk)
            self.check_object_permissions(self.request, poem)
            return poem
        except Poem.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        poem = self.get_object(pk)
        serializer = PoemSerializer(
            poem, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        poem = self.get_object(pk)
        serializer = PoemSerializer(
            poem, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        poem = self.get_object(pk)
        poem.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
