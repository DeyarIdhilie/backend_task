from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser

authorized_methods = ['POST','PUT', 'PATCH', 'DELETE']
safe_methods = ['GET']


class CustomPermissions(BasePermission):

    def has_permission(self, request, view):
        if (request.method in authorized_methods and
            request.user.is_authenticated and
            request.user.is_staff and request.user.is_superuser) or request.method in safe_methods:
            return True
        else:
            return False
