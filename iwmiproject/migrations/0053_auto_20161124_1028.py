# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0052_soilproperty_soil_depth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleharvestedcrop',
            name='crop',
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='distance_to_the_market',
            field=models.FloatField(blank=True, null=True, verbose_name='distance to the market(km)'),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='dripline_length',
            field=models.FloatField(blank=True, null=True, verbose_name='Drip line length(m)'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Amount sold'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='expenditure',
            field=models.FloatField(blank=True, null=True, verbose_name='Expenditure (Tsh)'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='income',
            field=models.FloatField(blank=True, null=True, verbose_name='Total income (Tsh)'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='net_income',
            field=models.FloatField(blank=True, null=True, verbose_name='Net income (Tsh)'),
        ),
    ]
