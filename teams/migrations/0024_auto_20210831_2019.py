# Generated by Django 3.1.4 on 2021-08-31 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0023_auto_20210831_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationparameters',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 31, 20, 19, 7, 236344)),
        ),
    ]
