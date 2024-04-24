from rest_framework import generics

from games.serializers import GameSerializer, UserGameSerializer
from games.models import Game, UserGame
from test.pagination import PaginationSize
from rest_framework.response import Response

# Create your views here.

class SaveGameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = PaginationSize

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "pk"

class AddGameToUser(generics.ListCreateAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    pagination_class = PaginationSize
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        game_data = request.data.get('game', {})

        igdb_id = game_data.get('igdb_id')

        # Busca una serie existente por tmdb_id
        try:
            game_instance = Game.objects.get(idgb_id=igdb_id)
        except Game.DoesNotExist:
            # Si no existe, crea una nueva serie
            game_serializer = GameSerializer(data=game_data)
            game_serializer.is_valid(raise_exception=True)
            game_instance = game_serializer.save()
        else:
            # Si existe, puedes tomar alguna acción adicional si es necesario
            pass

        # Crea una instancia de UserSerie relacionada con el usuario y la serie
        user_game_data = {'user_id': user_id, 'game': game_instance.id}
        user_game_serializer = UserGameSerializer(data=user_game_data)
        user_game_serializer.is_valid(raise_exception=True)
        user_anime_instance = user_game_serializer.save()

        # Devuelve una respuesta con los datos serializados de UserSerie y estado HTTP 201
        return Response(user_game_serializer.data, status=201)
    

class UserGameUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGame.objects.all()
    serializer_class = UserGameSerializer
    lookup_field = "pk"

class UserGames(generics.ListAPIView):
    serializer_class = UserGameSerializer
    pagination_class = PaginationSize

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserGame.objects.filter(user_id=user_id)
        return queryset
    