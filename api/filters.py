from .models import Client
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
