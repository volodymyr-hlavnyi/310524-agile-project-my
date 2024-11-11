# Generated by Django 5.1.3 on 2024-11-11 07:41

import apps.users.choices.positions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=apps.users.choices.positions.UserPositions.choices, default=apps.users.choices.positions.UserPositions['PROGRAMMER'], max_length=50),
        ),
    ]