# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0027_applicationcalibration_irrigated_depth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soilmoistureprofiler',
            name='measurement',
        ),
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='event',
            field=models.IntegerField(blank=True, verbose_name='Event number', null=True),
        ),
        migrations.AddField(
            model_name='soilmoistureprofiler',
            name='event',
            field=models.IntegerField(blank=True, verbose_name='Event number', null=True),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='event',
            field=models.IntegerField(blank=True, verbose_name='Event number', null=True),
        ),
    ]
