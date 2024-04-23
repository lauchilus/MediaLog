from rest_framework import generics

from games.serializers import GameSerializer, UserGameSerializer
from games.models import Game, UserGame

# Create your views here.

class SaveGameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "pk"

class AddGameToUser(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    

class UserGameUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    lookup_field = "pk"

class UserGames(generics.ListAPIView):
    serializer_class = UserGameSerializer

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserGame.objects.filter(user_id=user_id)
        return queryset
    