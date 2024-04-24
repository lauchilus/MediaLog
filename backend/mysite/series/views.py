from urllib import response
from rest_framework import generics
from rest_framework.response import Response

from test.pagination import PaginationSize
from series.models import Serie, UserSerie
from series.serializers import SerieSerializer, UserSerieSerializer

# Create your views here.

class SaveSerieView(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    pagination_class = PaginationSize

class SerieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    lookup_field = "pk"

class AddSerieToUser(generics.ListCreateAPIView):
    queryset = UserSerie.objects.all()
    serializer_class = UserSerieSerializer
    pagination_class = PaginationSize
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        serie_data = request.data.get('serie', {})

        tmdb_id = serie_data.get('tmdb_id')

        # Busca una serie existente por tmdb_id
        try:
            serie_instance = Serie.objects.get(tmdb_id=tmdb_id)
        except Serie.DoesNotExist:
            # Si no existe, crea una nueva serie
            serie_serializer = SerieSerializer(data=serie_data)
            serie_serializer.is_valid(raise_exception=True)
            serie_instance = serie_serializer.save()
        else:
            # Si existe, puedes tomar alguna acción adicional si es necesario
            pass

        # Crea una instancia de UserSerie relacionada con el usuario y la serie
        user_serie_data = {'user_id': user_id, 'serie': serie_instance.id}
        user_serie_serializer = UserSerieSerializer(data=user_serie_data)
        user_serie_serializer.is_valid(raise_exception=True)
        user_serie_instance = user_serie_serializer.save()

        # Devuelve una respuesta con los datos serializados de UserSerie y estado HTTP 201
        return Response(user_serie_serializer.data, status=201)


class UserSerieUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSerie.objects.all()
    serializer_class = UserSerieSerializer
    lookup_field = "pk"

class UserSeries(generics.ListAPIView):
    serializer_class = UserSerieSerializer
    pagination_class = PaginationSize

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserSerie.objects.filter(user_id=user_id)
        return queryset