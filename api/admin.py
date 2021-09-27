from django.contrib import admin
from .models import Client, Contract, Team, User, Event
from django.contrib import messages
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .function_admin import custom_titled_filter, StatusContract, StatusEvent, RoleUser


admin.site.site_header = "Admin Portal"



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
    list_filter = (
        ('company_name', custom_titled_filter('name of company')),
        ('date_created', DateRangeFilter),
    )

    def get_rangefilter_created_time_title(self, request, field_path):
        return 'Filter by creation date the contracts'

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

    # GET
    def has_view_permission(self, request, obj=None):
        return True

    # PUT
    def has_change_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    # DELETE
    def has_delete_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    # todo add foreingn key

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
    list_filter = (
        ('client', custom_titled_filter('name of clients')),
        ('created_time', DateRangeFilter),
        StatusContract,

    )



    def get_rangefilter_created_time_title(self, request, field_path):
        return 'Filter by creation date the contracts'


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

    # GET
    def has_view_permission(self, request, obj=None):
        return True

    # PUT
    def has_change_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    # DELETE
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
    fieldsets = [
        (
            "Event",
            {
                "fields": [
                    "title",
                    "contract",
                    "seller_contact",
                    "location_event",
                    "date_event",
                    "description",
                    "status",

                ]
            },
        ),
        (
            "Dates",
            {
                "fields": ["date_created"],
            },
        ),
    ]

    readonly_fields = ["date_created", "seller_contact", "contract"]
    list_filter = (

        ('contract__client', custom_titled_filter('name of clients')),
        ('contract', custom_titled_filter('name of contracts')),

        ('date_created', DateRangeFilter),
        StatusEvent,


    )

    def get_rangefilter_created_time_title(self, request, field_path):
        return 'Filter by creation date the event'

    def get_fieldsets(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER':
                self.readonly_fields = ['date_created']
            return self.fieldsets
        except:
            pass

    def has_add_permission(self, request):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER':
                return True
        except:
            return False

    def has_module_permission(self, request):
        return True

    # GET
    def has_view_permission(self, request, obj=None):
        return True

    # PUT
    def has_change_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    # DELETE
    def has_delete_permission(self, request, obj=None):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER' or obj.seller_contact == team:
                return True
        except:
            return False

    def save_model(self, request, obj, form, change):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER':
                obj.save()
        except:
            return messages.error(request, "You can't")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Team",
            {
                "fields": [
                    "user",
                    "role",
                ]
            },
        ),

    ]
    list_filter = (
        ('user__username', custom_titled_filter('name')),
        RoleUser,
    )

    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        try:
            team = Team.objects.get(user=request.user)
            if team.role == 'MANAGER':
                return True
            else:
                return False
        except:
            return False

    # GET
    def has_view_permission(self, request, obj=None):
        return True

    # PUT
    def has_change_permission(self, request, obj=None):
        return True

    # DELETE
    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.save()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
