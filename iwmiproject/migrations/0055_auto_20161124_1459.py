# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0054_applicationcalibration_dripline_numbers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth',
            field=models.FloatField(verbose_name='Measurement depth (cm)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='dripline_numbers',
            field=models.IntegerField(verbose_name='Number of drip lines', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tdrmeasurement',
            name='measurement',
            field=models.FloatField(verbose_name='Measurement(%)', blank=True, null=True),
        ),
    ]
