from django.contrib.auth import logout
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from ..utils.get_token import get_tokens_for_user
from ..utils.serializers.log_in_serializer import LoginSerializer


class LogInViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user is not None:
            token = get_tokens_for_user(user)

            return Response({'msg': 'Login Success', 'token': token}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
