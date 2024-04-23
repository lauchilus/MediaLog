from rest_framework import serializers

from games.models import Game, UserGame


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "igdb_id","name", "summary", "release_date", "poster_url"]

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = ["id", "user_id","game"]