# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0008_auto_20161013_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizermanagement',
            name='crop_stage',
            field=models.CharField(verbose_name='Crop Stage', default='o', max_length=40),
        ),
    ]
