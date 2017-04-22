# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0038_labourmanagament_time_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='area',
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='seeding_rate',
            field=models.FloatField(null=True, blank=True, verbose_name='seeding quantity'),
        ),
    ]
