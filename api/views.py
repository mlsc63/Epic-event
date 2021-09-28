from rest_framework import viewsets, permissions
from .models import Team, Client, Contract, Event, User
from .serializers import TeamSerializer, ClientSerializer, ContractSerializer, EventSerializer, UserSerializer
from .permissions import CreatorClient, CreatorContract, CreatorEvent, CreatorUser, CreatorTeam
from .filters import ClientFilter, ContractFilter, EventFilter
from django_filters import rest_framework as filters
import logging

logger = logging.getLogger(__name__)

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorClient]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def perform_create(self, serializer):
        try:
            team = Team.objects.get(user=self.request.user)
            serializer.save(seller_contact=team)
        except:
            logger.error('Something went wrong!')


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorContract]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContractFilter

    def get_queryset(self, *args, **kwargs):
        try:
            client = self.kwargs.get('client_pk')
            return Contract.objects.filter(client=client)
        except:
            logger.error('Something went wrong!')

    def perform_create(self, serializer):
        try:
            team = Team.objects.get(user=self.request.user)
            serializer.save(seller_contact=team)
        except:
            logger.error('Something went wrong!')


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorEvent]
    queryset = Event.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter


    def get_serializer(self, *args, **kwargs):

        try:
            serializer_class = EventSerializer
            user = Team.objects.get(user=self.request.user)
            if user.role == 'MANAGER':
                serializer_class.Meta.extra_kwargs.clear()

            kwargs['context'] = self.get_serializer_context()
            return serializer_class(*args, **kwargs)
        except:
            logger.error('Something went wrong!')


    def get_queryset(self, *args, **kwargs):
        try:
            client = Client.objects.get(pk=self.kwargs.get('client_pk'))
            contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'), client=client.id)
            return self.queryset.filter(contract=contract)
        except:
            logger.error('Something went wrong!')


    def perform_create(self, serializer):
        try:
            contract = Contract.objects.get(pk=self.kwargs.get('contract_pk'))
            serializer.save(contract=contract)
        except:
            logger.error('Something went wrong!')



class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorTeam]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & CreatorUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
