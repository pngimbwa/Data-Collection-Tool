# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0126_auto_20170113_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='calibrationcup_volume',
        ),
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='emitter_spacing',
        ),
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='emitter_wetted_diameter',
        ),
    ]
