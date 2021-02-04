# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-04 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebapp', '0005_auto_20191103_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='hospital_contact',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='police_contact',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='population',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='barth_rooms',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='garage',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='house_rooms',
            field=models.IntegerField(default='0'),
        ),
    ]