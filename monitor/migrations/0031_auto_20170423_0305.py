# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0030_profile_is_encrypt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='public_key',
            field=models.TextField(max_length=10000),
        ),
    ]
