# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0105_fertilizermanagement_nurseryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurseryirrigationevent',
            name='irrigation_depth',
            field=models.FloatField(null=True, blank=True, verbose_name='Irrigation depth'),
        ),
    ]
