# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0051_waterliftingcalibration_waterlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='soilproperty',
            name='soil_depth',
            field=models.FloatField(blank=True, null=True, verbose_name='soil depth(cm)'),
        ),
    ]
