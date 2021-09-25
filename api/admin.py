from django.contrib import admin
from .models import Client, Contract, Team, User, Event
from django.core.exceptions import PermissionDenied
from django.contrib import messages

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Client",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "company_name",
                    "seller_contact"
                ]
            },
        ),
        (
            "Dates",
            {
                "fields": ["date_created", "date_updated"],
            },
        ),
    ]

    readonly_fields = ["date_created", "date_updated", "seller_contact"]

    def get_fieldsets(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or request.user.is_superuser():
                self.readonly_fields.remove('seller_contact')
                return self.fieldsets
        except:
           return self.fieldsets


    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True

    #GET
    def has_view_permission(self, request, obj=None):
        return True

    #PUT
    def has_change_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
          return False

    #DELETE
    def has_delete_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False
    #todo add foreingn key

    def save_model(self, request, obj, form, change):
        team = Team.objects.get(user=request.user)
        if team.role == 'SELLER':
            obj.seller_contact = team
            obj.save()



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Contract",
            {
                "fields": [
                    "title",
                    "client",
                    "detail_event",
                    "amount",
                    "status",
                    "seller_contact"
                ]
            },
        ),
        (
            "Dates",
            {
                "fields": ["created_time"],
            },
        ),
    ]

    readonly_fields = ["created_time", "seller_contact"]

    def get_fieldsets(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or request.user.is_superuser():
                self.readonly_fields.remove('seller_contact')
                return self.fieldsets
        except:
           return self.fieldsets


    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True

    #GET
    def has_view_permission(self, request, obj=None):
        return True

    #PUT
    def has_change_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    #DELETE
    def has_delete_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    def save_model(self, request, obj, form, change):
        team = Team.objects.get(user=request.user)
        client = Client.objects.get(pk=obj.client.id)
        if client.seller_contact == team or team.role == 'MANGER':
            obj.seller_contact = team
            obj.save()
        else:
            return messages.error(request, "You can't")





@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
