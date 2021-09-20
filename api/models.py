from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    choice_role = [('SELLER', 'SELLER'), ('MANAGER', 'MANAGER')]

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="team_user")
    created_time = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=choice_role, default='SELLER')

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    company_name = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    seller_contact = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name="client_seller")

    def __str__(self):
        return "{}".format(self.first_name)


class Contract(models.Model):
    choice_status = [('UNSIGNED', 'UNSIGNED'), ('SIGNED', 'SIGNED')]

    title = models.CharField(max_length=20)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='contract_client')
    detail_event = models.TextField(null=True)
    amount = models.FloatField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=choice_status, default='UNSIGNED')
    seller_contact = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name="contract_seller")

    def __str__(self):
        return "{}".format(self.title)


class Event(models.Model):
    choice_status = [('TODO', 'TODO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('FINISHED', 'FINISHED')]

    title = models.CharField(max_length=150)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name='event_contract')
    seller_contact = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='event_seller')
    location_event = models.CharField(max_length=50)
    date_event = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=15, choices=choice_status, default="TODO")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)


class User(AbstractUser):
    pass
