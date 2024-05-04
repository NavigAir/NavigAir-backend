# Generated by Django 5.0.4 on 2024-05-04 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0001_initial'),
        ('User', '0007_remove_user_assigned_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='assigned_flight',
            field=models.ForeignKey(default='DEFAULT', on_delete=django.db.models.deletion.PROTECT, to='Flight.flight'),
        ),
    ]
