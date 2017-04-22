# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0050_residualhandling'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterliftingcalibration',
            name='waterlevel',
            field=models.FloatField(null=True, verbose_name='Total time(mins)', blank=True),
        ),
    ]
