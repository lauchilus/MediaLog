from rest_framework import generics

from books.serializers import BookSerializer, UserBookSerializer
from books.models import Book, UserBook

# Create your views here.
class SaveBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"

class AddBookToUser(generics.ListCreateAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    

class UserBookUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    lookup_field = "pk"

class UserBooks(generics.ListAPIView):
    serializer_class = UserBookSerializer

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserBook.objects.filter(user_id=user_id)
        return queryset
    