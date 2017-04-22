# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0056_applicationcalibration_calibration_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='calibration_cup_time',
            field=models.IntegerField(null=True, verbose_name='Calibration cup time(mins)', blank=True),
        ),
    ]
