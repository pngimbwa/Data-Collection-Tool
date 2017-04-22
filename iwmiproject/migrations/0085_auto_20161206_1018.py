# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0084_auto_20161202_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotirrigationevent',
            name='amount_used',
            field=models.FloatField(null=True, blank=True, verbose_name='Amount Used (Litre)'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='currency',
            field=models.CharField(max_length=10, null=True, blank=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='distance_from_water_source',
            field=models.FloatField(null=True, blank=True, verbose_name='Distance from water source(km)'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='fuel',
            field=models.ForeignKey(null=True, verbose_name='Fuel', blank=True, to='iwmiproject.Fuel'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='fuelcost',
            field=models.FloatField(null=True, blank=True, verbose_name='Total income'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='gender',
            field=models.CharField(max_length=10, null=True, blank=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='refilled_amount',
            field=models.FloatField(null=True, blank=True, verbose_name='Refilled amount (Litre)'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='technology',
            field=models.ForeignKey(null=True, verbose_name='Farm Technology', blank=True, to='iwmiproject.Technology'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='time_to_fetch_water',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken to fetch water'),
        ),
    ]
