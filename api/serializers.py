from .models import Team, User, Contract, Client, Event
from rest_framework import serializers, fields


class ClientSerializer(serializers.ModelSerializer):
    seller_contact = serializers.ReadOnlyField(source='seller_contact.id')

    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'seller_contact']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id',
                  'title',
                  'client',
                  'detail_event',
                  'amount',
                  'created_time',
                  'status']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id',
                  'title',
                  'contract',
                  'seller_contact',
                  'location_event',
                  'date_event',
                  'description',
                  'status',
                  'date_created']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'email',
                  'password']


class TeamSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M", read_only=True)

    class Meta:
        model = Team
        fields = ['id',
                  'user',
                  'role',
                  'created_time']

