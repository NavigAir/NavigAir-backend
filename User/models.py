from django.db import models
from django.core.exceptions import ValidationError

from Flight.models import Flight


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False)
    visual_percentage = models.IntegerField(null=False)
    mail = models.EmailField(null=False, unique=True)
    pwd = models.CharField(max_length=255, null=False, unique=True)
    dni = models.CharField(max_length=255, null=False, unique=True)
    passport = models.CharField(max_length=255, null=False, unique=True)
    address = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    assigned_flight = models.ForeignKey(Flight, on_delete=models.PROTECT, null=True)

    def clean(self):
        if self.visual_percentage < 0 or self.visual_percentage > 100:
            raise ValidationError({'visual_percentage': 'Visual percentage must be between 0 and 100.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Validación antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, primary_key=True)
    seat = models.CharField(max_length=255, null=False)
    fast_track = models.BooleanField(default=False, null=False)
    priority = models.BooleanField(default=False, null=False)
    bags = models.IntegerField(default=0, null=False)