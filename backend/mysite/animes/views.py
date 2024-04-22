from rest_framework import generics

from animes.models import Anime, UserAnime
from animes.serializers import AnimeSerializer, UserAnimeSerializer

# Create your views here.


class SaveAnimeView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class AnimeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = "pk"

class AddAnimeToUser(generics.ListCreateAPIView):
    queryset = UserAnime.objects.all()
    serializer_class = UserAnimeSerializer
    

class UserAnimeUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnime.objects.all()
    serializer_class = UserAnimeSerializer
    lookup_field = "pk"

class UserAnimes(generics.ListAPIView):
    serializer_class = UserAnimeSerializer

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserAnime.objects.filter(user_id=user_id)
        return queryset
    
