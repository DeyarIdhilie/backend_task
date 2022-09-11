from rest_framework import serializers
from .actor_serializer import ActorSerializer
from ...models.movie_actor import MovieActor


class MovieActorSerializer(serializers.ModelSerializer):
    actors = ActorSerializer( many=False)

    class Meta:
        model = MovieActor
        fields = ('id', 'movies', 'actors', 'created', 'updated')
        read_only_fields = ('movies', 'actors')



