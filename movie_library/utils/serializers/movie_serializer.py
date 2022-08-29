from rest_framework import serializers
from ...models.movie import Movie
from ...utils.serializers.trailer_serializer import TrailerSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated']


class MovieTrailerSerializer(MovieSerializer):
    trailers = serializers.SerializerMethodField("get_funct", source=Movie)
    trailers = TrailerSerializer(trailers, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated', "trailers"]

    def get_funct(self, obj):
        name = obj.trailers
        return name
