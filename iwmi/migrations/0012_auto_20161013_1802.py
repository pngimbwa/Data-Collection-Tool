# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0011_auto_20161013_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticidemanagement',
            name='crop_stage',
            field=models.CharField(verbose_name='Crop Stage', max_length=40),
        ),
        migrations.AlterField(
            model_name='pesticidemanagement',
            name='price',
            field=models.FloatField(verbose_name='Price(Tsh)'),
        ),
    ]
