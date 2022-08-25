
from ..models.movie import Movie
from .base_repository import BaseRepository
from ..models.trailer import Trailer
from ..utils.serializers.trailer_serializer import TrailerSerializer
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

    def create_movie(self, data):

        trailers = data.get('trailers')
        movie = Movie(title=data.get('title'), year=data.get('year'),duration=data.get('duration'),
                      release_date=data.get('release_date'))#, trailers=data.get('trailers'))
        movie.save()

        '''serializer = TrailerSerializer(data=trailers)
        if serializer.is_valid(raise_exception=True):
            trailers = serializer.save(movie=movie)'''
        bulk_list = list()
        for trailer in trailers:

            bulk_list.append(
                Trailer(movies=movie, url=trailer["url"]))

        bulk_msj = Trailer.objects.bulk_create(bulk_list)
        # for trailer in trailers:
        #     Trailer.objects.create(movies=movie, **trailer)
        #movie = Movie(**data)


        #movie.save()
        return movie

    def update_movie(self, movie, partial, data):

        if partial:
            movie.title = data.get("title", movie.title)
            movie.year = data.get("year", movie.year)
            movie.release_date = data.get("release_date", movie.release_date)
            movie.duration = data.get("duration", movie.duration)

        else:
            trailers = data.pop['trailers']
            for trailer in trailers:
                Trailer.objects.update(movies=movie, **trailer)
            movie.title = data.get("title")
            movie.year = data.get("year")
            movie.release_date = data.get("release_date")
            movie.duration = data.get("duration")

        movie.save()
        return movie




