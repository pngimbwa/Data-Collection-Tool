# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0014_auto_20161106_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bednursery',
            name='seedling_yield_per_bed',
        ),
        migrations.RemoveField(
            model_name='nursery',
            name='technology',
        ),
        migrations.AddField(
            model_name='seedmanagement',
            name='currency',
            field=models.CharField(max_length=10, verbose_name='Currency', default='Tsh'),
        ),
        migrations.AlterField(
            model_name='seedmanagement',
            name='price_per_unit',
            field=models.FloatField(verbose_name='Price per unit'),
        ),
        migrations.AlterField(
            model_name='seedmanagement',
            name='total_cost',
            field=models.FloatField(verbose_name='Total cost'),
        ),
    ]
