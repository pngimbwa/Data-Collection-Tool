# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0075_auto_20161128_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='total_plants',
            field=models.IntegerField(verbose_name='Total number of plants', null=True, blank=True),
        ),
    ]
