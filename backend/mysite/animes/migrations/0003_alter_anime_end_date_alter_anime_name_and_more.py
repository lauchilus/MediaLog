# Generated by Django 5.0.4 on 2024-04-25 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_useranime_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='anime',
            name='name',
            field=models.CharField(blank=True, default='No name provided', max_length=255),
        ),
        migrations.AlterField(
            model_name='anime',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='anime',
            name='synopsis',
            field=models.TextField(blank=True, default='No description provided'),
        ),
    ]
