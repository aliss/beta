# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0002_auto_20171213_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='alissuser',
            name='saved_services',
            field=models.ManyToManyField(blank=True, to='aliss.Service'),
        ),
    ]
