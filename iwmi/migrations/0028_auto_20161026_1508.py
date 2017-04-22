# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0027_auto_20161026_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmTotalPlotNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('number', models.IntegerField(verbose_name='Total plot numbers')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('plotID', models.CharField(verbose_name='Plot ID', max_length=50)),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='PlotManagement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('plot_size', models.FloatField(verbose_name='Plot size(sq.m)')),
                ('water_management_method', models.CharField(verbose_name='Water management method', max_length=80)),
                ('water_source', models.CharField(verbose_name='Water Source', max_length=80)),
                ('water_application', models.CharField(verbose_name='Water Application', max_length=80)),
                ('crop', models.ForeignKey(verbose_name='Crop', to='iwmi.Crop')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='PumpingSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='date')),
                ('source', models.CharField(verbose_name='Name', max_length=80)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('depth', models.FloatField(blank=True, verbose_name='Depth(m)', null=True)),
                ('diameter', models.FloatField(blank=True, verbose_name='Diameter(m)', null=True)),
            ],
            options={
                'ordering': ['depth'],
            },
        ),
        migrations.RemoveField(
            model_name='farmfields',
            name='fields',
        ),
        migrations.RemoveField(
            model_name='row',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='well',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='crop',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='pumping_source',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='soil_moisture_method',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='water_application',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='water_management_method',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='water_source',
        ),
        migrations.RemoveField(
            model_name='technologycalibration',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='technologyfailure',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='technologymanagement',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='tissuenutrientanalysis',
            name='rownumber',
        ),
        migrations.RemoveField(
            model_name='weed',
            name='crop',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='row',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='row',
        ),
        migrations.AddField(
            model_name='technologycalibration',
            name='farmer',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farmer', to='iwmi.People'),
        ),
        migrations.AddField(
            model_name='technologyfailure',
            name='farmer',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farmer', to='iwmi.People'),
        ),
        migrations.AddField(
            model_name='technologymanagement',
            name='farmer',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farmer', to='iwmi.People'),
        ),
        migrations.AlterField(
            model_name='technologyfailure',
            name='date',
            field=models.DateField(verbose_name='Failure date'),
        ),
        migrations.AlterField(
            model_name='technologymanagement',
            name='date',
            field=models.DateField(verbose_name='Received date'),
        ),
        migrations.DeleteModel(
            name='FarmFields',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
        migrations.DeleteModel(
            name='Well',
        ),
        migrations.AddField(
            model_name='pumpingsource',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm(s)', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='farm',
            field=models.ForeignKey(verbose_name='FieldID', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='plotID',
            field=models.ForeignKey(verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='plot',
            name='farm',
            field=models.ForeignKey(verbose_name='FieldID', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='plot',
            name='village',
            field=models.ForeignKey(verbose_name='Village', to='iwmi.Village'),
        ),
        migrations.AddField(
            model_name='farmtotalplotnumber',
            name='farm',
            field=models.ManyToManyField(verbose_name='Farm(s)', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='bedfarm',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot ID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='croppropertyfarm',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot ID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='farmirrigationevent',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot ID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='furrow',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot ID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Plot ID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='soilmoisturemeasurementmanagement',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='soilmoistureprofiler',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='soilproperty',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='tissuenutrientanalysis',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='weed',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='plotID',
            field=models.ForeignKey(blank=True, null=True, verbose_name='PlotID', to='iwmi.Plot'),
        ),
        migrations.AlterUniqueTogether(
            name='pumpingsource',
            unique_together=set([('latitude', 'longitude')]),
        ),
        migrations.AlterUniqueTogether(
            name='plot',
            unique_together=set([('village', 'plotID')]),
        ),
    ]
