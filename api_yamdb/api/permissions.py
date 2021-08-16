from rest_framework import permissions

from api_yamdb.settings import ROLES


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and
                    request.user.role == ROLES[2][0]))


class IsAdmin(permissions.BasePermission):
    """Доступ только администратору"""
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.role == ROLES[2][0])


class IsAuthorOrAdministratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_anonymous
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.role == ROLES[2][0]
            or request.user.role == ROLES[1][0]
        )
