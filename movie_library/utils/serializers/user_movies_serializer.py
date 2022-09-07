from ...models.user_movies import UserMovies
from rest_framework.serializers import ModelSerializer
from .movie_serializer import MovieSerializer
from django.contrib.auth.decorators import permission_required

class UserMoviesSerializer(ModelSerializer):
    movies = MovieSerializer(many=False)

    class Meta:
        model = UserMovies
        fields = ('id', 'users', 'movies', 'created', 'updated')
        read_only_fields = ('users', 'movies',)