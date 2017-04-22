# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0009_auto_20161105_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('water_management_method', models.CharField(max_length=80, verbose_name='Water management method')),
                ('yellow_depth_detector', models.FloatField(verbose_name='yellow_depth_detector(m)', null=True, blank=True)),
                ('red_depth_detector', models.FloatField(verbose_name='red_depth_detector(m)', null=True, blank=True)),
                ('rods_length', models.FloatField(verbose_name='red_depth_detector(m)', null=True, blank=True)),
                ('plotID', models.ForeignKey(to='iwmiproject.Plot', verbose_name='PlotID')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='rootdepth',
            field=models.FloatField(verbose_name='rootdepth(m)', null=True, blank=True),
        ),
    ]
