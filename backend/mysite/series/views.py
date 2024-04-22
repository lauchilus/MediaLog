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