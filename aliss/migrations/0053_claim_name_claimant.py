# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2021-04-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0052_auto_20200929_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='name_claimant',
            field=models.CharField(default='', max_length=100, verbose_name='Your name'),
        ),
    ]
