# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0035_auto_20161101_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedPlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('numbers', models.IntegerField(verbose_name='Number of beds')),
                ('planting_density', models.IntegerField(verbose_name='Planting density')),
                ('plotID', models.ForeignKey(null=True, blank=True, to='iwmi.Plot', verbose_name='Plot ID')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='PlotCropProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('root_depth', models.FloatField(verbose_name='Root depth (m)')),
                ('planting_spacing', models.FloatField(verbose_name='Planting space(cm)')),
                ('name', models.ForeignKey(verbose_name='Crop', to='iwmi.Crop')),
                ('plotID', models.ForeignKey(null=True, blank=True, to='iwmi.Plot', verbose_name='Plot ID')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.RemoveField(
            model_name='bedfarm',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='bedfarm',
            name='plotID',
        ),
        migrations.RemoveField(
            model_name='croppropertyfarm',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='croppropertyfarm',
            name='name',
        ),
        migrations.RemoveField(
            model_name='croppropertyfarm',
            name='plotID',
        ),
        migrations.DeleteModel(
            name='BedFarm',
        ),
        migrations.DeleteModel(
            name='CropPropertyFarm',
        ),
    ]
