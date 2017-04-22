# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0120_auto_20161230_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='nurseryID_one',
            field=models.CharField(max_length=10, null=True, blank=True, verbose_name='nurseryID for Crop One'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='nurseryID_two',
            field=models.CharField(max_length=10, null=True, blank=True, verbose_name='nurseryID for Crop Two'),
        ),
    ]
