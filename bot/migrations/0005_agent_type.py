# Generated by Django 3.1.4 on 2022-07-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_agent_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='type',
            field=models.CharField(choices=[('rasa', 'rasa'), ('dialogflow', 'dialogflow')], default='rasa', max_length=20),
            preserve_default=False,
        ),
    ]
