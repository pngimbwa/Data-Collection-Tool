# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0057_applicationcalibration_calibration_cup_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantingmethod',
            old_name='seeding_rate',
            new_name='seed_quantity',
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='number_of_plants_per_row',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of plants per row'),
        ),
    ]
