# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-03 05:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0002_auto_20191103_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='owner',
            new_name='user',
        ),
    ]
