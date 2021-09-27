from abc import ABC
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Event

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter, ABC):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper

class StatusContract(SimpleListFilter):
    """
    This filter is being used in django admin panel in profile model.
    """
    title = 'Status of contracts'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('UNSIGNED', 'Unsigned'),
            ('SIGNED', 'Signed'),
            ('S_B_N_E', 'Signed but not event create'),

        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().upper() == 'UNSIGNED':
            return queryset.filter(status="UNSIGNED")
        elif self.value().upper() == 'SIGNED': 
            return queryset.filter(status="SIGNED")
        elif self.value().upper() == 'S_B_N_E':
            return queryset.exclude(id__in=[elem.contract.status == 'SIGNED' for elem in Event.objects.all()])

class ContractSignedWithoutEvent(SimpleListFilter):
    """
    This filter is being used in django admin panel in profile model.
    """
    title = 'Without Event'
    parameter_name = 'exist'

    def lookups(self, request, model_admin):
        return (
            ('S_B_N_E', 'Signed but not event create'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().upper() == 'S_B_N_E':
            return queryset.filter(event_contract__status='SIGNED')




