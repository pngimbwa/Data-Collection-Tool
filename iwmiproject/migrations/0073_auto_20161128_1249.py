# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0072_remove_saleharvestedcrop_net_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='fare',
            field=models.FloatField(blank=True, null=True, verbose_name='Fare'),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='fuel_cost',
            field=models.FloatField(blank=True, null=True, verbose_name='Total income'),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='fuel_type',
            field=models.ForeignKey(blank=True, verbose_name='Fuel', null=True, to='iwmiproject.Fuel'),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='mode_of_transport',
            field=models.CharField(max_length=22, blank=True, null=True, verbose_name='Total income'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='income',
            field=models.FloatField(blank=True, null=True, verbose_name='Total income'),
        ),
    ]
