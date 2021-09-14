from django.contrib import admin
from .models import Client, Contract, Team, Event, User


admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Event)