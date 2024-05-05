from django.db import models
from django.core.exceptions import ValidationError

from Flight.models import Flight


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=True)
    visual_percentage = models.IntegerField(null=False)
    mail = models.EmailField(null=False, unique=True)
    pwd = models.CharField(max_length=255, null=False, unique=True)
    passport = models.CharField(max_length=255, null=False, unique=True)
    address = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    assigned_flight = models.ForeignKey(Flight, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, primary_key=True)
    seat = models.CharField(max_length=255, null=False)
    fast_track = models.BooleanField(default=False, null=False)
    priority = models.BooleanField(default=False, null=False)
    bags = models.IntegerField(default=0, null=False)