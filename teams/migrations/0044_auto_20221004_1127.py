# Generated by Django 3.1.4 on 2022-10-04 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0043_auto_20221004_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationparameters',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 11, 27, 31, 6701)),
        ),
    ]
