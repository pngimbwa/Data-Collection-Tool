# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0010_auto_20161013_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticidemanagement',
            name='crop_stage',
            field=models.CharField(default='o', max_length=40, verbose_name='Crop Stage'),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='price',
            field=models.FloatField(verbose_name='Price(Tsh)', default=0),
        ),
    ]
