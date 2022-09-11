from rest_framework import serializers
from ...utils.serializers.movie_actor_serializer import MovieActorSerializer
from ...models.movie import Movie
from ...utils.serializers.trailer_serializer import TrailerSerializer
from ...utils.serializers.image_serializer import ImageSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated']


class MovieTrailerSerializer(MovieSerializer):
    trailers = serializers.SerializerMethodField("get_trailers", source=Movie)
    trailers = TrailerSerializer(trailers, many=True)
    actors = serializers.SerializerMethodField("get_actors")
    actors = MovieActorSerializer(actors, many=True)
    images = serializers.SerializerMethodField("get_actors")
    images = ImageSerializer(images, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'year', 'release_date', 'created', 'updated', "trailers", 'actors', 'images']

    def get_trailers(self, movie_object):
        trailers = movie_object.trailers
        return trailers

    def get_actors(self, movie_object):
        actors = movie_object.actors
        return actors

    def get_images(self, movie_object):
        images = movie_object.images
        return images