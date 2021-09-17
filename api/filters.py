from .models import Client
import django_filters
from django_filters import rest_framework as filters



class ClientFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='iexact')
    last_name = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(lookup_expr='iexact')
    phone = django_filters.CharFilter(lookup_expr='iexact')
    company_name = django_filters.CharFilter(lookup_expr='iexact')
    date_created = django_filters.DateFilter(lookup_expr='iexact')
    date_updated = django_filters.DateFilter(lookup_expr='iexact')
    seller_contact = django_filters.CharFilter(lookup_expr='iexact')



    class Meta:
        model = Client
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'seller_contact',
                  'sort_by']
