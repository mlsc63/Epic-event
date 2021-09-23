# from django.contrib import admin
# from .models import Client, Contract, Team, Event, User


# admin.site.register(Client)
# admin.site.register(Contract)
# admin.site.register(Team)
# admin.site.register(User)
# admin.site.register(Event)

from django.contrib import admin
from .models import Client, Contract, Team, User, Event


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                 'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'phone',
                    'company_name',
                    # 'date_created',
                    # 'date_updated',
                    'seller_contact'
                 ),

            }),
    )
    readonly_fields = ('date_created', 'date_updated')

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields



    # Permet d'avoir une autorisation d'acceder au panel -> staff_status -> True
    def has_add_permission(self, request):
        return True

    #permet d'afficher le module Client
    def has_module_permission(self, request):
        return True

    # GET
    def has_view_permission(self, request, obj=None):
        return True

    #PUT
    def has_change_permission(self, request, obj=None):
        return True
    #DELETE
    def has_delete_permission(self, request, obj=None):
        return True







@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    amount = 'contract__amount'
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
