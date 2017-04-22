# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0154_plotcrop_cropping_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='sub_plot_plant_number',
            field=models.FloatField(null=True, blank=True, verbose_name='Number of plants in the sub-plot'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='sub_plot_size',
            field=models.FloatField(null=True, blank=True, verbose_name='Sub plot size(sq.m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='total_plant_number',
            field=models.IntegerField(null=True, blank=True, verbose_name='Total number of plants'),
        ),
    ]
