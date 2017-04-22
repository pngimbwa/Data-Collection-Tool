# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0042_auto_20161123_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='pump',
        ),
        migrations.AddField(
            model_name='service',
            name='currency',
            field=models.CharField(verbose_name='Price Unit', blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='distance_to_shop',
            field=models.FloatField(blank=True, verbose_name='Distance to shop(km)', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, null=True, verbose_name='Farm'),
        ),
        migrations.AddField(
            model_name='service',
            name='maintenance_place',
            field=models.CharField(verbose_name='Maintenance place', blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='technology_broken',
            field=models.CharField(verbose_name='Technology broken', blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='travel_cost',
            field=models.FloatField(blank=True, verbose_name='Travel cost', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='group',
            field=models.ForeignKey(to='iwmiproject.FarmGroup', blank=True, null=True, verbose_name='FarmGroup'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(blank=True, verbose_name='Price of spaire parts', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_cost',
            field=models.FloatField(blank=True, verbose_name='Total repaire cost', null=True),
        ),
    ]
