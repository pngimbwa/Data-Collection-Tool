# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0132_auto_20170124_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_planting_method',
            field=models.CharField(null=True, blank=True, max_length=20, verbose_name='Planting Method'),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_planting_method',
            field=models.CharField(null=True, blank=True, max_length=20, verbose_name='Planting Method'),
        ),
    ]
