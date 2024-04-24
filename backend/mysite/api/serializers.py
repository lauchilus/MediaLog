from rest_framework import serializers

from .models import Movie, UserMovies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id","tmdb_id","name","overview","release_date","poster_url"]

class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovies
        fields = ["id","user_id","movie","date"]