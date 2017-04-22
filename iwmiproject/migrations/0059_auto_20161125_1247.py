# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0058_auto_20161125_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingmethod',
            name='number_of_plants_per_row',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='plantsnumber',
        ),
    ]
