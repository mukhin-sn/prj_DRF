from rest_framework.permissions import BasePermission

from users.models import Roles


class IsModer(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == Roles.MODERATOR:
            return True
        return False


class IsMaster(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.master:
            return True
        return False
