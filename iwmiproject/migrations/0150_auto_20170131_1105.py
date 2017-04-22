# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0149_auto_20170128_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotirrigationevent',
            name='time_to_fill_water_tank',
            field=models.FloatField(blank=True, verbose_name='Total time to fill water tank(mins)', null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='water_level_aftr_filling',
            field=models.FloatField(blank=True, verbose_name='Water level after filling(cm)', null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='water_level_bf_filling',
            field=models.FloatField(blank=True, verbose_name='Water level before filling(cm)', null=True),
        ),
    ]
