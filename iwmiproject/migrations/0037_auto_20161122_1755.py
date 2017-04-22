# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0036_auto_20161121_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationcalibration',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='End time', blank=True),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='Start time', blank=True),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='total_time',
            field=models.FloatField(null=True, verbose_name='Total time(mins)', blank=True),
        ),
    ]
