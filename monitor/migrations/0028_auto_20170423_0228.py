# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 17:28
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0027_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='fuzzerFile',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location=b'/Users/sweetchip/Desktop/Code_Repository/dev_sweetmon/sweetmon/files/fuzzer/'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='testcaseFile',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location=b'/Users/sweetchip/Desktop/Code_Repository/dev_sweetmon/sweetmon/files/testcase/'), upload_to=b''),
        ),
    ]
