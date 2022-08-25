from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from ..utils.serializers.register_serializer import RegisterSerializer


class UserViewSet( ViewSet):
    def create(self, request):
        data = request.data
        user = User.objects.create(
         username=data['username'],
         email=data['email'],
         first_name=data['first_name'],
         last_name=data['last_name']
    )

        user.set_password(data['password'])
        user.save()

        result = RegisterSerializer(user)
        response = Response(data=result.data, status=201)

        return response
