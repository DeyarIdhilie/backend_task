from rest_framework import serializers
from .actor_serializer import ActorSerializer
# from .movie_serializer import MovieSerializer
from ...models.movie_actor import MovieActor


class MovieActorSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField("get_funct")
    actors = ActorSerializer(actors, many=False)
    # movies = serializers.SerializerMethodField("get_function")
    # movies = MovieSerializer(movies, many=False)

    class Meta:
        model = MovieActor
        fields = ('id', 'movies', 'actors', 'created', 'updated')
        read_only_fields = ('movies', 'actors')

    def get_funct(self, obj):
        name = obj.actors
        return name

    # def get_function(self, obj):
    #     name = obj.movies
    #     return name