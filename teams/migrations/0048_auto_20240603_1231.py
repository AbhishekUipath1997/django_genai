# Generated by Django 3.1.4 on 2024-06-03 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0047_auto_20240603_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationparameters',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 3, 12, 31, 30, 307640)),
        ),
    ]
