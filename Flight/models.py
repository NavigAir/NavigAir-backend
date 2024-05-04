from django.db import models

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

