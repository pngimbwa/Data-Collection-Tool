# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0166_yieldfarmlevel_quantity_harvested'),
    ]

    operations = [
        migrations.AddField(
            model_name='tissuenutrientanalysis',
            name='bed_number',
            field=models.IntegerField(null=True, verbose_name='Bed/Row number', blank=True),
        ),
    ]
