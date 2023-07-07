from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPagination

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    pagination_class = CustomPagination
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


