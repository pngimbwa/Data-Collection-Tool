# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0066_remove_saleharvestedcrop_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='row_number',
            field=models.IntegerField(verbose_name='Row number', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterliftingcalibration',
            name='waterlevel',
            field=models.FloatField(verbose_name='Water level(m)', blank=True, null=True),
        ),
    ]
