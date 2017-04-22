# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0045_auto_20161101_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotIrrigationEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('irrigation_event', models.IntegerField(verbose_name='Irrigation Event')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time(mins)')),
                ('quantification_method', models.CharField(max_length=30, verbose_name='Quantification method')),
                ('flume_location', models.CharField(max_length=30, verbose_name='Flume location')),
                ('waterlevel1', models.FloatField(verbose_name='Water level 1')),
                ('waterlevel2', models.FloatField(blank=True, null=True, verbose_name='Water level 2')),
                ('furrow_irr_time', models.FloatField(verbose_name='Time to irrigate one furrow (mins)')),
                ('nfurrorws_irrigated_once', models.FloatField(verbose_name='Number of furrow irrigated at once')),
                ('application_rate', models.FloatField(blank=True, null=True, verbose_name='Application rate(m3/s)')),
                ('standardvolume', models.FloatField(blank=True, null=True, verbose_name='Standard volume')),
                ('quantity_of_units', models.IntegerField(blank=True, null=True, verbose_name='Quantity of unit')),
                ('yellow_WFD_before_irrigation', models.IntegerField(blank=True, null=True, verbose_name='Yellow WFD before irrigation')),
                ('red_WFD_before_irrigation', models.IntegerField(blank=True, null=True, verbose_name='Red WFD before irrigation')),
                ('yellow_WFD_time_after_irrigation', models.FloatField(blank=True, null=True, verbose_name='Yellow WFD time after irrigation')),
                ('red_WFD_time_after_irrigation', models.FloatField(blank=True, null=True, verbose_name='Red WFD time after irrigation')),
                ('climate', models.CharField(max_length=20, verbose_name='Climate')),
                ('plotID', models.ForeignKey(to='iwmi.Plot', blank=True, null=True, verbose_name='PlotID')),
                ('technology', models.ForeignKey(to='iwmi.Technology', verbose_name='Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='farmirrigationevent',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='farmirrigationevent',
            name='plotID',
        ),
        migrations.RemoveField(
            model_name='farmirrigationevent',
            name='technology',
        ),
        migrations.AlterModelOptions(
            name='harvest',
            options={'ordering': ['plotID']},
        ),
        migrations.RemoveField(
            model_name='tissuenutrientanalysis',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='weed',
            name='farm',
        ),
        migrations.AddField(
            model_name='harvest',
            name='plotID',
            field=models.ForeignKey(to='iwmi.Plot', blank=True, null=True, verbose_name='Harvested farm'),
        ),
        migrations.AlterField(
            model_name='tissuenutrientanalysis',
            name='ca',
            field=models.FloatField(verbose_name='Calcium(%)'),
        ),
        migrations.AlterField(
            model_name='tissuenutrientanalysis',
            name='mg',
            field=models.FloatField(verbose_name='Magnesium(%)'),
        ),
        migrations.AlterField(
            model_name='tissuenutrientanalysis',
            name='s',
            field=models.FloatField(verbose_name='Sulphur(%)'),
        ),
        migrations.AlterUniqueTogether(
            name='harvest',
            unique_together=set([('plotID', 'date')]),
        ),
        migrations.DeleteModel(
            name='FarmIrrigationEvent',
        ),
        migrations.RemoveField(
            model_name='harvest',
            name='farm',
        ),
    ]
