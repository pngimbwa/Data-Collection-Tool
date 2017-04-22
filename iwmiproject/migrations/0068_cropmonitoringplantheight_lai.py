# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0067_auto_20161128_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='LAI',
            field=models.FloatField(null=True, verbose_name='leaf area index (LAI) ', blank=True),
        ),
    ]
