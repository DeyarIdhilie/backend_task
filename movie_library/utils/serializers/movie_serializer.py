from rest_framework import serializers
from ...utils.serializers.movie_actor_serializer import MovieActorSerializer
from ...models.movie import Movie
from ...utils.serializers.trailer_serializer import TrailerSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated']


class MovieTrailerSerializer(MovieSerializer):
    trailers = serializers.SerializerMethodField("get_trailers", source=Movie)
    trailers = TrailerSerializer(trailers, many=True)
    actors = serializers.SerializerMethodField("get_actors")
    actors = MovieActorSerializer(actors, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated', "trailers", 'actors']

    def get_trailers(self, movie_object):
        trailers = movie_object.trailers
        return trailers

    def get_actors(self, movie_object):
        actors = movie_object.actors
        return actors
