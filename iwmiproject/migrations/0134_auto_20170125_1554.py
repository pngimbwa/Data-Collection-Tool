# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0133_auto_20170124_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingmethod',
            name='planting_method',
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='date',
            field=models.DateField(null=True, blank=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_planting_method',
            field=models.CharField(null=True, blank=True, verbose_name='Crop_one planting Method', max_length=20),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_planting_method',
            field=models.CharField(null=True, blank=True, verbose_name='Crop_two planting Method', max_length=20),
        ),
    ]
