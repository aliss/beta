# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-07-14 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0042_claim_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
