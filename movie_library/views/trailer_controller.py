from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..models.movie import Movie
from ..models.trailer import Trailer
from ..utils.serializers.trailer_serializer import TrailerSerializer


class TrailerViewSet(ViewSet):

    def list(self, request, domain_pk=None):
        queryset = Trailer.objects.all()
        trailers = queryset.filter(movies=domain_pk)
        result = TrailerSerializer(trailers, many=True)
        return Response(data=result.data, status=200)

    def create(self, request, domain_pk=None):
        data = request.data
        new_trailer = Trailer.objects.create(movies=Movie.objects.get(id=domain_pk), url=data["url"])
        new_trailer.save()
        result = TrailerSerializer(new_trailer)
        return Response(result.data, status=201)

    def retrieve(self, request, pk=None, domain_pk=None):
        queryset = Trailer.objects.all()
        trailers = queryset.get(pk=pk, movies=domain_pk)
        result = TrailerSerializer(trailers, many=False)
        return Response(data=result.data, status=200)

    def update(self, request, pk=None, domain_pk=None):
        data = request.data
        queryset = Trailer.objects.all()
        trailer = queryset.get(pk=pk, movies=domain_pk)
        trailer.url = data.get("url")
        trailer.save()
        result = TrailerSerializer(trailer, many=False)
        return Response(data=result.data, status=200)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None, domain_pk=None):
        queryset = Trailer.objects.all()
        trailer = queryset.get(pk=pk, movies=domain_pk)
        trailer.delete()
        response_message = {"item has been deleted"}
        return Response(response_message, status=status.HTTP_204_NO_CONTENT)
