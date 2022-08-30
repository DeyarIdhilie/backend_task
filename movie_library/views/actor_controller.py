from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models.movie import Movie
from ..models.actor import Actor
from ..utils.serializers.actor_serializer import ActorSerializer
from ..utils.serializers.actor_movies_serializer import ActorMoviesSerializer
from ..models.movie_actor import MovieActor

class ActorViewSet(ViewSet):

    def list(self, request):
        actors = Actor.objects.all()
        result = ActorSerializer(actors, many=True)
        return Response(data=result.data, status=200)

    def create(self, request):
        data = request.data
        movies = data.get('movies')
        actor = Actor(first_name=data.get('first_name'),last_name=data.get('last_name'),gender=data.get('gender'))
        actor.save()
        bulk_list = list()
        query = Movie.objects.all()
        for movie in movies:
            the_movie = get_object_or_404(query, pk=movie)
            bulk_list.append(
                MovieActor(actors=actor, movies=the_movie))

        bulk_msj = MovieActor.objects.bulk_create(bulk_list)
        result = ActorMoviesSerializer(actor, many=False)
        return Response(data=result.data, status=201)

    def retrieve(self, request, pk=None):
        actors = Actor.objects.all()
        actor = get_object_or_404(actors, pk=pk)
        serializer = ActorMoviesSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset,pk=pk)
        actor.delete()
        response_message = {"item has been deleted"}
        return Response(response_message, status=status.HTTP_204_NO_CONTENT)

