from rest_framework import serializers
from ...models.trailer import Trailer
#from .movie_serializer import MovieSerializer

class TrailerSerializer(serializers.ModelSerializer):

    #movie = MovieSerializer(read_only=True)
    class Meta:
        model = Trailer
        fields = ('id','movies', 'url', 'created', 'updated')
        read_only_fields = ('movies',)
