# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aliss', '0021_organisation_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='image',
            new_name='logo',
        ),
    ]
