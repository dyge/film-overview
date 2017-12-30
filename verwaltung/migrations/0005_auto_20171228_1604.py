# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verwaltung', '0004_auto_20171228_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ('-titel',)},
        ),
        migrations.AddField(
            model_name='film',
            name='bew',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True),
        ),
    ]