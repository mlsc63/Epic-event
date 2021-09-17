from rest_framework import permissions
from .models import Team

class CreatorClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user = Team.objects.get(user=request.user)

        if (obj.seller_contact == user) or (user.role == 'MANAGER'):
            return True
        else:
            return False
