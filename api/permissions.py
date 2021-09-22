from rest_framework import permissions
from .models import Team, Client


# All user can read, just creator and manager can modified
class CreatorClient(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user = Team.objects.get(user=request.user)

        if (obj.seller_contact == user) or (user.role == 'MANAGER'):
            return True
        else:
            return request.method in ["GET"]


# All user can read, just creator and manager can modified
class CreatorContract(permissions.BasePermission):

    def has_permission(self, request, view):
        user = Team.objects.get(user=request.user)
        query_client = view.kwargs.get('client_pk')
        client = Client.objects.get(pk=query_client)
        if (client.seller_contact == user) or (user.role == 'MANAGER'):
            return True
        else:
            return request.method in ["GET"]

    def has_object_permission(self, request, view, obj):
        user = Team.objects.get(user=request.user)

        if (obj.seller_contact == user) or (user.role == 'MANAGER'):
            return True
        else:
            return request.method in ["GET"]


class CreatorEvent(permissions.BasePermission):

    def has_permission(self, request, view):
        team = Team.objects.get(user=request.user)
        if team.role == 'MANAGER':
            return True
        else:
            return request.method in ["GET", "DELETE", "PUT"]

    def has_object_permission(self, request, view, obj):
        team = Team.objects.get(user=request.user)
        if team.role == 'MANAGER':
            return True
        elif obj.seller_contact == team:
            print('ok')
            return request.method in ["GET", "PUT"]
        else:
            return request.method in ["GET"]


class CreatorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        team = Team.objects.get(user=request.user)
        if team.role == 'MANAGER':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True


class CreatorTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        team = Team.objects.get(user=request.user)
        if team.role == 'MANAGER':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True
