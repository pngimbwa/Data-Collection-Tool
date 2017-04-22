# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0013_auto_20161105_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='seedmanagement',
            name='seed_spacing_btn_bed',
            field=models.FloatField(null=True, verbose_name='seed spacing btn bed/row(m)', blank=True),
        ),
        migrations.AddField(
            model_name='seedmanagement',
            name='seed_spacing_within_a_bed',
            field=models.FloatField(null=True, verbose_name='seed spacing within a bed/row(m)', blank=True),
        ),
    ]
