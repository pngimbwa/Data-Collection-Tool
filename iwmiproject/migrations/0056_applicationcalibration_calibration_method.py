# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0055_auto_20161124_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='calibration_method',
            field=models.CharField(verbose_name='Calibration method', max_length=20, null=True, blank=True),
        ),
    ]
