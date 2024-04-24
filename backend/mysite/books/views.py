from rest_framework import generics

from test.pagination import PaginationSize
from books.serializers import BookSerializer, UserBookSerializer
from books.models import Book, UserBook
from rest_framework.response import Response

# Create your views here.
class SaveBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PaginationSize

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"

class AddBookToUser(generics.ListCreateAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    pagination_class = PaginationSize

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        book_data = request.data.get('book', {})

        open_library_id = book_data.get('open_library_id')

        # Busca una serie existente por tmdb_id
        try:
            book_instance = Book.objects.get(open_library_id=open_library_id)
        except Book.DoesNotExist:
            # Si no existe, crea una nueva serie
            book_serializer = BookSerializer(data=book_data)
            book_serializer.is_valid(raise_exception=True)
            book_instance = book_serializer.save()
        else:
            # Si existe, puedes tomar alguna acción adicional si es necesario
            pass

        # Crea una instancia de UserSerie relacionada con el usuario y la serie
        user_book_data = {'user_id': user_id, 'book': book_instance.id}
        user_book_serializer = UserBookSerializer(data=user_book_data)
        user_book_serializer.is_valid(raise_exception=True)
        user_book_instance = user_book_serializer.save()

        # Devuelve una respuesta con los datos serializados de UserSerie y estado HTTP 201
        return Response(user_book_serializer.data, status=201)
    

class UserBookUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    lookup_field = "pk"

class UserBooks(generics.ListAPIView):
    serializer_class = UserBookSerializer
    pagination_class = PaginationSize

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        queryset = UserBook.objects.filter(user_id=user_id)
        return queryset
    