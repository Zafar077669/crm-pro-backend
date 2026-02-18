from rest_framework.permissions import BasePermission


class IsOwnerOrAssigned(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.owner == request.user
            or obj.assigned_to == request.user
        )
