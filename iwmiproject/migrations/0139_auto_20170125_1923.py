# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0138_plantingmethod_planting_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotmanagement',
            name='mulching_quantity',
            field=models.FloatField(blank=True, verbose_name='Mulching quantity (Kg)', null=True),
        ),
    ]
