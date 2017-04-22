# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0167_tissuenutrientanalysis_bed_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='marketprice',
            field=models.FloatField(blank=True, null=True, verbose_name='Market price'),
        ),
    ]
