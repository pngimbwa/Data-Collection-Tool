# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0009_fertilizermanagement_crop_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizermanagement',
            name='crop_stage',
            field=models.CharField(verbose_name='Crop Stage', max_length=40),
        ),
    ]
