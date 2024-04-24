from rest_framework import generics

from animes.models import Anime, UserAnime
from animes.serializers import AnimeSerializer, UserAnimeSerializer
from test.pagination import PaginationSize
from rest_framework.response import Response

# Create your views here.


class SaveAnimeView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    pagination_class = PaginationSize

class AnimeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = "pk"

    

class AddAnimeToUser(generics.ListCreateAPIView):
    queryset = UserAnime.objects.all()
    serializer_class = UserAnimeSerializer
    pagination_class = PaginationSize

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        anime_data = request.data.get('anime', {})

        mal_id = anime_data.get('mal_id')

        # Busca una serie existente por tmdb_id
        try:
            anime_instance = Anime.objects.get(mal_id=mal_id)
        except Anime.DoesNotExist:
            # Si no existe, crea una nueva serie
            anime_serializer = AnimeSerializer(data=anime_data)
            anime_serializer.is_valid(raise_exception=True)
            anime_instance = anime_serializer.save()
        else:
            # Si existe, puedes tomar alguna acción adicional si es necesario
            pass

        # Crea una instancia de UserSerie relacionada con el usuario y la serie
        user_anime_data = {'user_id': user_id, 'anime': anime_instance.id}
        user_anime_serializer = UserAnimeSerializer(data=user_anime_data)
        user_anime_serializer.is_valid(raise_exception=True)
        user_anime_instance = user_anime_serializer.save()

        # Devuelve una respuesta con los datos serializados de UserSerie y estado HTTP 201
        return Response(user_anime_serializer.data, status=201)
    

class UserAnimeUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnime.objects.all()
    serializer_class = UserAnimeSerializer
    lookup_field = "pk"

class UserAnimes(generics.ListAPIView):
    serializer_class = UserAnimeSerializer
    pagination_class = PaginationSize

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserAnime.objects.filter(user_id=user_id)
        return queryset
    
