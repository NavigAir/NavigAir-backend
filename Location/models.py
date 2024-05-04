from django.db import models
from django.utils.translation import gettext_lazy as _

class LocationType(models.TextChoices):
    SECURITY_CONTROL = 'security_control', _('Security Control')
    WC = 'wc', _('WC')
    BOARDING_DOOR = 'boarding_door', _('Boarding Door')

class Location(models.Model):
    latitude = models.CharField(max_length=100, null=False)
    longitude = models.CharField(max_length=100, null=False)
    type = models.CharField(
        max_length=50,
        choices=LocationType.choices,
    )

    def __str__(self):
        return f"{self.type} at {self.latitude}, {self.longitude}"

class BoardingDoor(Location):
    code = models.CharField(max_length=100, null=False)
    finger = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.type != LocationType.BOARDING_DOOR:
            raise ValueError("BoardingDoor instances must have type set to 'boarding_door'.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - Finger: {'Yes' if self.finger else 'No'}"