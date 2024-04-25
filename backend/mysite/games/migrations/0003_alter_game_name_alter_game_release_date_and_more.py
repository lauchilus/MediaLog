# Generated by Django 5.0.4 on 2024-04-25 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_usergame_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, default='No name provided', max_length=255),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='game',
            name='summary',
            field=models.TextField(default='No description provided'),
        ),
    ]