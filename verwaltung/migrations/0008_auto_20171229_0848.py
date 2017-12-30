# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verwaltung', '0007_auto_20171229_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='qual',
            field=models.CharField(choices=[('sehr gut', 'sehr gut'), ('gut', 'gut'), ('mittel', 'mittel'), ('schlecht', 'schlecht')], default='Kein Eintrag', max_length=100),
        ),
    ]
