# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0061_house_elevation'),
    ]

    operations = [
        migrations.AddField(
            model_name='pumpingsource',
            name='elevation',
            field=models.FloatField(verbose_name="Source's longitude", blank=True, null=True),
        ),
    ]
