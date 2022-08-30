from ..repositories.movie_repository import MovieRepository
from ..models.movie import Movie
from django.shortcuts import get_object_or_404


class MovieComponent:
    """
    this used for applying any needed logic
    """

    @staticmethod
    def get_movies():
        # no login needed
        return MovieRepository().get_movies()

    @staticmethod
    def get_movie(pk):
        queryset = MovieComponent.get_movies()
        movie = get_object_or_404(queryset, pk=pk)
        return movie

    # @staticmethod
    def is_movie_exist(data):
        is_exist = True
        if Movie.objects.filter(title=data.get("title")).exists():
            is_exist = False
        return is_exist

    @staticmethod
    def create_new_movie(data):
        movie = MovieRepository().create_movie(data)
        return movie

    @staticmethod
    def check_if_all_fields(data):

        if data.get("title") and data.get("year") and data.get("release_date") and data.get(
                "duration"):

            return True
        else:

            return False

    def update_movie(self, movie, partial, data):

        changed_movie = MovieRepository().update_movie(movie, partial, data)
        return changed_movie
