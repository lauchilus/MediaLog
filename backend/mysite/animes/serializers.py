from rest_framework import serializers

from animes.models import Anime, UserAnime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ["id","mal_id","name","synopsis","release_date","end_date","poster_url"]

class UserAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnime
        fields = ["id", "user_id","anime","date"]