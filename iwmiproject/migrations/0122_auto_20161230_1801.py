# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0121_auto_20161230_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantingmethod',
            name='total_plants',
            field=models.FloatField(null=True, verbose_name='Total number of plants', blank=True),
        ),
    ]
