# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0019_auto_20161106_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseryirrigationevent',
            name='discharge',
        ),
        migrations.RemoveField(
            model_name='nurseryirrigationevent',
            name='standard_volume',
        ),
        migrations.AlterField(
            model_name='nurseryirrigationevent',
            name='quantity',
            field=models.FloatField(null=True, blank=True, verbose_name='Quantity(Number of buckets)'),
        ),
    ]
