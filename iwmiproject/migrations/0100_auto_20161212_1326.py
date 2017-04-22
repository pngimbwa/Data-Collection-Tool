# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0099_auto_20161209_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropvarieties',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', null=True, verbose_name='FarmID', blank=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_10',
            field=models.FloatField(blank=True, verbose_name='Measurement at 10cm(%)', null=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_100',
            field=models.FloatField(blank=True, verbose_name='Measurement at 100cm(%)', null=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_20',
            field=models.FloatField(blank=True, verbose_name='VMeasurement at 20cm(%)', null=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_30',
            field=models.FloatField(blank=True, verbose_name='Measurement at 30cm(%)', null=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_40',
            field=models.FloatField(blank=True, verbose_name='Measurement at 40cm(%)', null=True),
        ),
        migrations.AlterField(
            model_name='soilmoistureprofiler',
            name='depth_60',
            field=models.FloatField(blank=True, verbose_name='Measurement at 60cm(%)', null=True),
        ),
    ]
