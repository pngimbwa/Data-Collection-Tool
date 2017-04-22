# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0035_auto_20161121_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='number_of_bad_plants',
        ),
        migrations.RemoveField(
            model_name='plotmanagement',
            name='number_of_good_plants',
        ),
        migrations.RemoveField(
            model_name='plotmanagement',
            name='plant_density_per_bed',
        ),
        migrations.RemoveField(
            model_name='plotmanagement',
            name='plant_density_per_sqm',
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of bad plants'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of good plants'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_density_per_bed',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density per bed'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_density_per_sqm',
            field=models.FloatField(blank=True, null=True, verbose_name='plant density per sq.m'),
        ),
    ]
