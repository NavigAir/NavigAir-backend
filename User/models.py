from django.db import models
from django.core.exceptions import ValidationError

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

    def clean(self):
        if self.visual_percentage < 0 or self.visual_percentage > 100:
            raise ValidationError({'visual_percentage': 'Visual percentage must be between 0 and 100.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Validación antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
