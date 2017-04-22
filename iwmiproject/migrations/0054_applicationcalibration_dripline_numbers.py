# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0053_auto_20161124_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='dripline_numbers',
            field=models.IntegerField(null=True, verbose_name='CNumber of drip lines', blank=True),
        ),
    ]
