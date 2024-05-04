from django.db import models

from Location.models import BoardingDoor


class Flight(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True)
    origin = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=True)
    departure_time = models.TimeField(null=False)
    arrival_time = models.TimeField(null=False)
    date = models.DateField(null=False)
    company = models.CharField(max_length=255, null=False)
    plane = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.id

class Boarding(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    boarding_door = models.ForeignKey(BoardingDoor, on_delete=models.CASCADE, primary_key=True)
    opening_time = models.TimeField(null=False)
    last_call = models.TimeField(null=False)
    opened = models.BooleanField(default=False, null=False)
