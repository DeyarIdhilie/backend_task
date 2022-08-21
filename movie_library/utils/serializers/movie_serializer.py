
from rest_framework import serializers

from ...models.movie import Movie


class MovieSerializer(serializers.ModelSerializer):
    #actors=
    class Meta:
        model = Movie
        fields = ['id','title','duration','year','release_date']
