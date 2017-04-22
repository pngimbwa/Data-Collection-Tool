# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0025_auto_20161110_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationCalibration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('water_application', models.CharField(max_length=80, verbose_name='Water Application')),
                ('bucketdiameter', models.FloatField(null=True, blank=True, verbose_name='Bucket diameter(cm)')),
                ('bucketvolume', models.FloatField(null=True, blank=True, verbose_name='Bucket volume(L)')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time(mins)')),
                ('application_rate', models.FloatField(null=True, blank=True, verbose_name='Application rate(mm/hr)')),
                ('bucketnumbers', models.FloatField(null=True, blank=True, verbose_name='Number of buckets')),
                ('waterheight', models.FloatField(null=True, blank=True, verbose_name='Water height(cm)')),
                ('topfurrowwidth', models.FloatField(null=True, blank=True, verbose_name='Top furrow width(cm)')),
                ('buttonfurrowwidth', models.FloatField(null=True, blank=True, verbose_name='Button furrow width(cm)')),
                ('wetteddiameteraroundplant', models.FloatField(null=True, blank=True, verbose_name='Wetted diameter around plant(cm)')),
                ('irrigate_whole_or_per_plant', models.CharField(null=True, max_length=20, blank=True, verbose_name='Irrigate whole or per plant')),
                ('field_efficiency', models.FloatField(null=True, blank=True, verbose_name='Field efficiency(%)')),
                ('conveyance_efficiency', models.FloatField(null=True, blank=True, verbose_name='Conveyance efficiency(%)')),
                ('dripline_length', models.FloatField(null=True, blank=True, verbose_name='Drip line length(cm)')),
                ('dripline_spacing', models.FloatField(null=True, blank=True, verbose_name='Drip line spacing(cm)')),
                ('emitter_spacing', models.FloatField(null=True, blank=True, verbose_name='Emitter spacing(cm)')),
                ('driptank_volume', models.FloatField(null=True, blank=True, verbose_name='Drip tank volume (L)')),
                ('calibrationcup_volume', models.FloatField(null=True, blank=True, verbose_name='Calibration cup volume(L)')),
                ('emitter_wetted_diameter', models.FloatField(null=True, blank=True, verbose_name='Emitter wetted diameter(cm)')),
                ('plot', models.ForeignKey(to='iwmiproject.Plot', verbose_name='Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
