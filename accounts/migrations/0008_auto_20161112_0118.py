# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20161110_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secrethashcode',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 12, 1, 17, 57, 484380)),
        ),
    ]
