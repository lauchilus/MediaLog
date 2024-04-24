


from rest_framework import serializers

from series.models import Serie, UserSerie


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ["id","tmdb_id","name","overview","release_date","poster_url"]

class UserSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerie
        fields = ["id","user_id","serie","date"]