# Generated by Django 3.1.4 on 2022-07-15 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0029_auto_20220715_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationparameters',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 11, 45, 44, 400422)),
        ),
    ]
