from rest_framework.permissions import BasePermission

from users.models import Roles


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Roles.MODERATOR


class IsMaster(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.master
