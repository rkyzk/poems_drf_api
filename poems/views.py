from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poem
from .serializers import PoemSerializer


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
