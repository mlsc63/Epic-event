from .models import Client, Contract, Event
import django_filters


class ClientFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='iexact')
    last_name = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(lookup_expr='iexact')
    phone = django_filters.CharFilter(lookup_expr='iexact')
    company_name = django_filters.CharFilter(lookup_expr='iexact')
    date_created = django_filters.NumberFilter(lookup_expr='year')
    date_updated = django_filters.NumberFilter(lookup_expr='year')
    seller_contact = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        order_by_field = 'date_created',
        model = Client
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'seller_contact',
                  ]


class ContractFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='iexact')
    client = django_filters.CharFilter(lookup_expr='iexact')
    detail_event = django_filters.CharFilter(lookup_expr='iexact')
    amount = django_filters.NumberFilter(lookup_expr='iexact')
    created_time = django_filters.NumberFilter(lookup_expr='year')
    status = django_filters.CharFilter(lookup_expr='iexact')
    seller_contact = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        order_by_field = 'date_created',
        model = Contract
        fields = ['title',
                  'client',
                  'detail_event',
                  'amount',
                  'created_time',
                  'status',
                  'seller_contact',
                  ]

class EventFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='iexact')
    contract = django_filters.CharFilter(lookup_expr='iexact')
    seller_contact = django_filters.CharFilter(lookup_expr='iexact')
    location_event = django_filters.CharFilter(lookup_expr='iexact')
    date_event = django_filters.NumberFilter(lookup_expr='year')
    description = django_filters.CharFilter(lookup_expr='iexact')
    status = django_filters.CharFilter(lookup_expr='iexact')
    date_created = django_filters.NumberFilter(lookup_expr='year')

    class Meta:
        order_by_field = 'date_created',
        model = Event
        fields = ['title',
                  'contract',
                  'seller_contact',
                  'location_event',
                  'date_event',
                  'description',
                  'status',
                  'date_created',
                  ]
