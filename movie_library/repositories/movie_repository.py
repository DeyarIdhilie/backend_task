from ..models.movie import Movie
from .base_repository import BaseRepository
from ..models.trailer import Trailer


class MovieRepository:

    def get_movies(self, filters=None):
        query = BaseRepository().get_base_query(Movie, filters)
        return query.all()

    def create_movie(self, data):

        trailers = data.get('trailers')
        movie = Movie(title=data.get('title'), year=data.get('year'), duration=data.get('duration'),
                      release_date=data.get('release_date'))
        movie.save()
        bulk_list = list()
        for trailer in trailers:
            bulk_list.append(
                Trailer(movies=movie, url=trailer["url"]))

        bulk_msj = Trailer.objects.bulk_create(bulk_list)
        return movie

    def update_movie(self, movie, partial, data):

        if partial:
            movie.title = data.get("title", movie.title)
            movie.year = data.get("year", movie.year)
            movie.release_date = data.get("release_date", movie.release_date)
            movie.duration = data.get("duration", movie.duration)

        else:

            movie.title = data.get("title")
            movie.year = data.get("year")
            movie.release_date = data.get("release_date")
            movie.duration = data.get("duration")
            movie.save()

        return movie
