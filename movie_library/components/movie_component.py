from ..repositories.movie_repository import MovieRepository
from ..models.movie import Movie
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import BadRequest
from django.shortcuts import render, get_object_or_404


class MovieComponent():
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
        try:
            if not (Movie.objects.filter(title=data.get("title")).exists()):
                print("hiiiii")
                return True
        except:

            # raise BadRequest( 'this movie already exsit')
            return False
        ''' content = {'this movie already exist'}
              return Response(content, status=status.HTTP_400_BAD_REQUEST)
               else:'''

    @staticmethod
    def create_new_movie(data):
        movie = MovieRepository().create_movie(**data)
        return movie

    @staticmethod
    def check_if_all_fields(**data):


            if data.get("title")  and data.get("year") and data.get("release_date") and data.get(
                    "duration"):

                return True
            else:

             return False

    def update_movie(self,movie, **data):
        changed_movie = MovieRepository().update_movie(movie, **data)
        return changed_movie


    def update_movie_partially(self, movie, **data):
       changed_movie = MovieRepository().update_movie_partially(movie, **data)
       return changed_movie