# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-03-01 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet', '0005_ability_boost_flaw_free'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ability_boost_flaw',
            name='free',
        ),
    ]