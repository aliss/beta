# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0009_auto_20180131_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='alissuser',
            name='prepopulate_postcode',
            field=models.BooleanField(default=False),
        ),
    ]
