# Generated by Django 5.0.4 on 2024-05-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_checkin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dni',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
