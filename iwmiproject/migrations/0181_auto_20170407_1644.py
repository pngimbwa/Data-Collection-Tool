# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0180_auto_20170407_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_eigth',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_five',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_four',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_nine',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_one',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_seven',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_six',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_ten',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_three',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth_two',
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth',
            field=models.FloatField(verbose_name='Measurement depth (cm)', null=True, blank=True),
        ),
    ]
