from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..models.actor import Actor
from ..utils.serializers.actor_serializer import ActorSerializer


class ActorViewSet(ViewSet):

    def list(self, request):
        actors = Actor.objects.all()
        result = ActorSerializer(actors, many=True)
        return Response(data=result.data, status=200)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
