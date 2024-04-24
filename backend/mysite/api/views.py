from rest_framework import generics

from api.models import Movie, UserMovies
from api.serializers import MovieSerializer, UserMovieSerializer
from test.pagination import PaginationSize
from rest_framework.response import Response

# Create your views here.

class SaveMovieView(generics.ListCreateAPIView):        
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        pagination_class = PaginationSize
   
class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        lookup_field = "pk"

class AddMovieToUser(generics.ListCreateAPIView):
        queryset = UserMovies.objects.all()
        serializer_class = UserMovieSerializer
        pagination_class = PaginationSize

        def post(self, request, *args, **kwargs):
                user_id = request.data.get('user_id')
                movie_data = request.data.get('movie', {})

                tmdb_id = movie_data.get('tmdb_id')

                # Busca una serie existente por tmdb_id
                try:
                        movie_instance = Movie.objects.get(tmdb_id=tmdb_id)
                except Movie.DoesNotExist:
                # Si no existe, crea una nueva serie
                        movie_serializer = MovieSerializer(data=movie_data)
                        movie_serializer.is_valid(raise_exception=True)
                        movie_instance = movie_serializer.save()
                else:
                # Si existe, puedes tomar alguna acción adicional si es necesario
                        pass

                # Crea una instancia de UserSerie relacionada con el usuario y la serie
                user_movie_data = {'user_id': user_id, 'movie': movie_instance.id}
                user_movie_serializer = UserMovieSerializer(data=user_movie_data)
                user_movie_serializer.is_valid(raise_exception=True)
                user_movie_instance = user_movie_serializer.save()

                # Devuelve una respuesta con los datos serializados de UserSerie y estado HTTP 201
                return Response(user_movie_serializer.data, status=201)

class UserMoviesUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = UserMovies.objects.all()
        serializer_class = UserMovieSerializer
        lookup_field = "pk"

class UserMoviesList(generics.ListAPIView):
    serializer_class = UserMovieSerializer
    pagination_class = PaginationSize

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserMovies.objects.filter(user_id=user_id)
        return queryset