from rest_framework import generics

from series.models import Serie, UserSerie
from series.serializers import SerieSerializer, UserSerieSerializer

# Create your views here.

class SaveSerieView(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SerieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    lookup_field = "pk"

class AddSerieToUser(generics.ListCreateAPIView):
    queryset = UserSerie.objects.all()
    serializer_class = UserSerieSerializer

class UserSerieUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSerie.objects.all()
    serializer_class = UserSerieSerializer
    lookup_field = "pk"

class UserSeries(generics.ListAPIView):
    serializer_class = UserSerieSerializer

    def get_queryset(self):
        # Obtener el parámetro user_id de la URL
        user_id = self.kwargs['user_id']

        # Filtrar los animes asociados al user_id proporcionado
        queryset = UserSerie.objects.filter(user_id=user_id)
        return queryset