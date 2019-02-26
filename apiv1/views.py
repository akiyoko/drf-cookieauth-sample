from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from shop.models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if int(request.query_params.get('page', 0)) < 0:
            raise APIException("指定されたページは存在しません")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, pk, **kwargs):
        return super().update(request, pk, *args, **kwargs)
