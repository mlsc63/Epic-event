from rest_framework import viewsets, permissions
from .models import Team, Client, Contract, Event, User
from .serializers import TeamSerializer, ClientSerializer, ContractSerializer, EventSerializer, UserSerializer
from .permissions import CreatorClient, CreatorContract, CreatorEvent, CreatorUser, CreatorTeam
from .filters import ClientFilter, ContractFilter, EventFilter
from django_filters import rest_framework as filters


#
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
    permission_classes = [permissions.IsAuthenticated & CreatorContract]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContractFilter

    def get_queryset(self, *args, **kwargs):
        client = self.kwargs.get('client_pk')
        return Contract.objects.filter(client=client)

    def perform_create(self, serializer):
        team = Team.objects.get(user=self.request.user)
        serializer.save(seller_contact=team)


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorEvent]
    queryset = Event.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    # on Initialise le serialisateur pour pouvoir mocker extra_kwargs,
    # et avoir l'instance de l'utilisateur pour savoir son status
    def get_serializer(self, *args, **kwargs):
        #ini serializer
        serializer_class = EventSerializer
        user = Team.objects.get(user=self.request.user)
        if user.role == 'MANAGER':
            serializer_class.Meta.extra_kwargs.clear()

        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


    def get_queryset(self, *args, **kwargs):
        client = Client.objects.get(pk=self.kwargs.get('client_pk'))
        contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'), client=client.id)
        return self.queryset.filter(contract=contract)


    def perform_create(self, serializer):
        contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'))
        serializer.save(contract=contract)



class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorTeam]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
