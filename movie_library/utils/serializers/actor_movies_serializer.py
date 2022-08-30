from rest_framework import serializers

from ...models.actor import Actor
from .actor_serializer import ActorSerializer
from .movie_serializer import MovieSerializer


class ActorMoviesSerializer(ActorSerializer):
    movies = serializers.SerializerMethodField("get_function")
    movies = MovieSerializer(movies, many=True)

    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'gender', 'created', 'updated', 'movies']

    def get_function(self, obj):
        movies = obj.movies
        return movies