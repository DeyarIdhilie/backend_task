from rest_framework import serializers
#from .movie_actor_serializer import MovieActorSerializer
#from .movie_serializer import MovieSerializer
from ...models.actor import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'gender', 'created', 'updated']




