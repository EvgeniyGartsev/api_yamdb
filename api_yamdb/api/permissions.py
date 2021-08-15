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


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
    """Author or staff can edit the review."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            or request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff
