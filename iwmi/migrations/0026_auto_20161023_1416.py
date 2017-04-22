# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0025_auto_20161018_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilMoistureMeasurementManagement',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement_option', models.CharField(max_length=75, verbose_name='Soil measurement used(option)')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='lenght_of_crop_stage',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='planting_date',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='personels',
        ),
        migrations.RemoveField(
            model_name='harvest',
            name='harvest_personel',
        ),
        migrations.RemoveField(
            model_name='harvest',
            name='payement',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='id',
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='length_of_crop_stage',
            field=models.FloatField(verbose_name='Length of crop stage(days)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='price_unit',
            field=models.FloatField(verbose_name='Price Unit', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='price_unit',
            field=models.FloatField(verbose_name='Price Unit', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width',
            field=models.FloatField(verbose_name='Plant canopy width(m)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_height',
            field=models.FloatField(verbose_name='Plant height(m)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row',
            field=models.IntegerField(verbose_name='Row Number', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fertilizermanagement',
            name='price',
            field=models.FloatField(verbose_name='Price', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='amount_for_home',
            field=models.FloatField(verbose_name='Harvest amount for home(Kg)'),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='amount_for_sell',
            field=models.FloatField(verbose_name='Harvest amount for sell(Kg)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Phone', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pesticidemanagement',
            name='price',
            field=models.FloatField(verbose_name='Price', blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='pumpownership',
            name='name',
        ),
        migrations.AddField(
            model_name='pumpownership',
            name='name',
            field=models.ForeignKey(to='iwmi.Pump', verbose_name='Name', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(serialize=False, max_length=100, primary_key=True, verbose_name='Technology'),
        ),
        migrations.AlterField(
            model_name='yieldrowbedlevel',
            name='row',
            field=models.IntegerField(verbose_name='Row Number', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='soilmoisturemeasurementmanagement',
            name='farm',
            field=models.ForeignKey(to='iwmi.Farm', verbose_name='Farm'),
        ),
    ]
