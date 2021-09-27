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
            ('S_B_N_E', 'Signed but not event created'),

        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().upper() == 'UNSIGNED':
            return queryset.filter(status="UNSIGNED")
        elif self.value().upper() == 'SIGNED':
            return queryset.filter(status="SIGNED")
        elif self.value().upper() == 'S_B_N_E':
            return queryset.exclude(
                id__in=[elem.contract.status == 'SIGNED'
                        for elem in Event.objects.all()
                        ])

class StatusEvent(SimpleListFilter):
    """
        This filter is being used in django admin panel in profile model.
        """
    title = 'Status of events'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('TODO', 'Todo'),
            ('IN_PROGRESS', 'In progress'),
            ('FINISHED', 'Finished'),

        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().upper() == 'TODO':
            return queryset.filter(status="TODO")
        elif self.value().upper() == 'IN_PROGRESS':
            return queryset.filter(status="IN_PROGRESS")
        elif self.value().upper() == 'FINISHED':
            return queryset.filter(status='FINISHED')

class RoleUser(SimpleListFilter):
    """
            This filter is being used in django admin panel in profile model.
            """
    title = 'Status of users'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('SELLER', 'Seller'),
            ('MANAGER', 'Manager'),

        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().upper() == 'SELLER':
            return queryset.filter(role="SELLER")
        elif self.value().upper() == 'MANAGER':
            return queryset.filter(role="MANAGER")








