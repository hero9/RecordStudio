# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20161104_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='duration',
        ),
    ]