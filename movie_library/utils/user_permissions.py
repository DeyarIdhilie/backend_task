from rest_framework.permissions import BasePermission, IsAuthenticated
import jwt
from django.conf import settings
from rest_framework.response import Response


class UserPermissions(BasePermission):

    def check_object_permissions(self,request,obj):
        print("check permissions")
        if request.user.is_authenticated:
            token = request.headers.get('Authorization')
            token = str.replace(str(token), 'Bearer ', '')
            decoded_payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_payload['user_id']
            if user_id == int(obj.id):
                return True
            else:
                return False
        else:
            return False


    '''def has_permission(self, request, view):
        return UserPermissions().has_object_permission(request, view)
        

    def has_object_permission(self, request, view, obj):
        print("check permissions")
        if request.user.is_authenticated:
            # Token.objects.get(key=request.auth.key).user_id
            # token = request.META.get('HTTP_AUTHORIZATION')
            token = request.headers.get('Authorization')
            token = str.replace(str(token), 'Bearer ', '')
            # token_parts= token.split('\\.')
            decoded_payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_payload['user_id']
            # decode_payload= base64.b64decode(token_parts[1])
            # user_id = token['user_id']
            # user = CustomUser.objects.get(id=user_id)
            # result = RegisterSerializer(user, many=False)
            # return Response(data=result.data)
            # return Response(user_id)
            print(user_id)
            print(obj.id)
            if user_id == int(obj.id):
                return True
            else:
                return False
        else:
            return False'''
