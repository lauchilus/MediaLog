from rest_framework import generics

from api.models import Movie, UserMovies
from api.serializers import MovieSerializer, UserMovieSerializer

# Create your views here.

class SaveMovieView(generics.ListCreateAPIView):        
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer

   
class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        lookup_field = "pk"

class AddMovieToUser(generics.ListCreateAPIView):
        queryset = UserMovies.objects.all()
        serializer_class = UserMovieSerializer

class UserMoviesUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = UserMovies.objects.all()
        serializer_class = UserMovieSerializer
        lookup_field = "pk"

class UserMoviesList(generics.ListAPIView):
    serializer_class = UserMovieSerializer

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserMovies.objects.filter(user_id=user_id)
        return queryset