# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0080_auto_20161130_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotirrigationevent',
            name='tanknumber',
            field=models.IntegerField(verbose_name='Red WFD time after irrigation', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterliftingcalibration',
            name='discharge',
            field=models.FloatField(verbose_name='Discharge(L/s)', blank=True, null=True),
        ),
    ]
