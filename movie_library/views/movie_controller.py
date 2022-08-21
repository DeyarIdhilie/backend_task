from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ..components.movie_component import MovieComponent
from ..models.movie import Movie
from ..utils.serializers.movie_serializer import MovieSerializer
from ..repositories.movie_repository import MovieRepository

class MovieViewSet(ViewSet):

    def list(self, request):

        movies = MovieComponent.get_movies()
        result = MovieSerializer(movies, many=True)
        return Response(data=result.data, status=200)

    def create(self, request):

        request_data = request.data
        flag = MovieComponent.is_movie_exist(request_data)

        #try:
        if flag == True:
             #movie.save()
             movie = MovieComponent.create_new_movie(request_data)
             result = MovieSerializer(movie, many=False)
             return Response(data=result.data, status=201)
        #except:
            #serializer = MovieSerializer(Movie(request_data))
        else:
          return Response('There is a movie with this title',status=status.HTTP_400_BAD_REQUEST)
            #raise ValueError('No file found')

    def retrieve(self, request, pk=None):

        movie = MovieComponent.get_movie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
      try:
        movie_before = MovieComponent.get_movie(pk)
        data = request.data
        #movie_after = MovieComponent.check_if_all_fields(movie_before, **data)
        flag = MovieComponent.check_if_all_fields(**data)

        if flag == True:
            movie_after= MovieComponent().update_movie(movie_before, **data)
            serializer = MovieSerializer(movie_after)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif flag == False:
            print ("hello")
            return Response("U need to enter all the field", status=status.HTTP_400_BAD_REQUEST)
      except:
          return Response("no movie with this id", status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            movie_before = MovieComponent.get_movie(pk)
            data = request.data
            movie_after = MovieComponent().update_movie_partially(movie_before, **data)
            serializer = MovieSerializer(movie_after)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response("no movie with this id", status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        movie = MovieComponent.get_movie(pk)
        movie.delete()
        response_message = {"item has been deleted"}
        return Response(response_message , status=status.HTTP_204_NO_CONTENT)