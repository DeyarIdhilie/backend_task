from rest_framework import serializers
from ...models.trailer import Trailer


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = ('id', 'movies', 'url', 'created', 'updated')
        read_only_fields = ('movies',)
