from rest_framework.permissions import BasePermission


class IsMaster(BasePermission):
    def has_object_permission(self, request, view, obj):
        pass
