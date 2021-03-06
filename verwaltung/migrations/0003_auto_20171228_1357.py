# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verwaltung', '0002_auto_20171228_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(choices=[('Comedy', 'Comedy'), ('Horror', 'Horror'), ('Action', 'Action'), ('Fantasy', 'Fantasy'), ('Drama', 'Drama'), ('Adventure', 'Adventure'), ('Sci-fi', 'Sci-fi'), ('Animation', 'Animation'), ('Crime', 'Crime'), ('Mystery', 'Mystery'), ('Romance', 'Romance')], max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
