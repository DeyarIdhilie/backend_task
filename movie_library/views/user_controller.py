from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..utils.serializers.register_serializer import RegisterSerializer
from ..models.users import CustomUser


class UserViewSet(ViewSet):
    def create(self, request):
        data = request.data
        user = CustomUser.objects.create(

            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            gender=data['gender'],
            is_superuser=data['is_superuser'],
            is_staff=data['is_staff']
        )

        user.set_password(data['password'])
        user.save()

        result = RegisterSerializer(user)

        response = Response(data=result.data, status=201)

        return response
