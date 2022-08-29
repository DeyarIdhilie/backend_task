from django.contrib.auth import login, authenticate, logout
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, permissions, serializers

from ..utils.get_token import get_tokens_for_user
from ..utils.serializers.log_in_serializer import LoginSerializer
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.

class LogInViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)

    #@csrf_exempt
    def create(self, request):
        # data = request.data
        # serializer = serializers.LoginSerializer(data=data,
        #                                      context={'request': self.request})
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # login(request, user)
        # return Response(None, status=status.HTTP_202_ACCEPTED)
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def create(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)