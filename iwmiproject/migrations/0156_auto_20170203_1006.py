# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0155_auto_20170203_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_density_per_bed',
            field=models.IntegerField(null=True, verbose_name='Plant density per bed', blank=True),
        ),
    ]
