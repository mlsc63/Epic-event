from rest_framework import viewsets, permissions
from .models import Team, Client, Contract, Event, User
from .serializers import TeamSerializer, ClientSerializer, ContractSerializer, EventSerializer, UserSerializer
from .permissions import CreatorClient
from .filters import ClientFilter
from django_filters import rest_framework as filters

class ClientViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated & CreatorClient]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def perform_create(self, serializer):
        team = Team.objects.get(user=self.request.user)
        serializer.save(seller_contact=team)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer