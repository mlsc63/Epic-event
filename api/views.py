from rest_framework import viewsets, permissions
from .models import Team, Client, Contract, Event, User
from .serializers import TeamSerializer, ClientSerializer, ContractSerializer, EventSerializer, UserSerializer
from .permissions import CreatorClient, CreatorContract
from .filters import ClientFilter
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

    def get_queryset(self, *args, **kwargs):
        client = self.kwargs.get('client_pk')
        return Contract.objects.filter(client=client)


    def perform_create(self, serializer):
        team = Team.objects.get(user=self.request.user)
        serializer.save(seller_contact=team)

    #def perform_create(self, serializer):
    #    print(serializer)
    #    team = Team.objects.get(user=self.request.user)
    #    save = serializer.save(seller_contact=team)

    #    if self.request.data['status'] == 'SIGNED':
    #        print(save.id)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self, *args, **kwargs):
        client = Client.objects.get(pk=self.kwargs.get('client_pk'))
        contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'), client=client.id)
        return self.queryset.filter(contract=contract)


    def perform_create(self, serializer):
        contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'))
        serializer.save(contract=contract)











class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
