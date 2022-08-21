
from ..models.movie import Movie
from .base_repository import BaseRepository

class MovieRepository():
    """
    this is used to perform the ORM operation and all database operations
    """

    '''def get_base_query(self, filters=None, **options):
        return Movie.objects.all()

    def get_movies(self, filters=None):
        query = self.get_base_query(filters)
        return query.all()'''

    def get_movies(self, filters=None):
        query = BaseRepository().get_base_query(Movie, filters)
        return query.all()

    def create_movie(self, **data):

        movie = Movie(**data)
        movie.save()
        return movie

    def update_movie(self, movie , **data):

        movie.title = data.get("title")
        movie.year = data.get("year")
        movie.release_date = data.get("release_date")
        movie.duration = data.get("duration")
        movie.save()
        return movie

    def update_movie_partially(self , movie, **data):

        movie.title = data.get("title", movie.title)
        movie.year = data.get("year", movie.year)
        movie.release_date = data.get("release_date", movie.release_date)
        movie.duration = data.get("duration", movie.duration)
        movie.save()
        return movie
