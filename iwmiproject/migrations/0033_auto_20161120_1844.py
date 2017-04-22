# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0032_applicationcalibration_enteredpersonel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='standardvolume',
        ),
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='technology',
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='bucketdiameter',
            field=models.FloatField(verbose_name='Bucket diameter(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='bucketnumbers',
            field=models.FloatField(verbose_name='Number of buckets', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='bucketvolume',
            field=models.FloatField(verbose_name='Bucket volume(L)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='buttonfurrowwidth',
            field=models.FloatField(verbose_name='Button furrow width(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='calibrationcup_volume',
            field=models.FloatField(verbose_name='Calibration cup volume(L)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='conveyance_efficiency',
            field=models.FloatField(verbose_name='Conveyance efficiency(%)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='dripline_length',
            field=models.FloatField(verbose_name='Drip line length(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='dripline_spacing',
            field=models.FloatField(verbose_name='Drip line spacing(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='driptank_volume',
            field=models.FloatField(verbose_name='Drip tank volume (L)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='emitter_spacing',
            field=models.FloatField(verbose_name='Emitter spacing(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='emitter_wetted_diameter',
            field=models.FloatField(verbose_name='Emitter wetted diameter(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='field_efficiency',
            field=models.FloatField(verbose_name='Field efficiency(%)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='irrigate_whole_or_per_plant',
            field=models.CharField(max_length=20, verbose_name='Irrigate whole or per plant', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='irrigated_depth',
            field=models.FloatField(verbose_name='Irrigated depth(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='topfurrowwidth',
            field=models.FloatField(verbose_name='Top furrow width(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='water_application',
            field=models.CharField(max_length=80, verbose_name='Water Application', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='waterheight',
            field=models.FloatField(verbose_name='Water height(cm)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='wetteddiameteraroundplant',
            field=models.FloatField(verbose_name='Wetted diameter around plant(cm)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='application_rate',
            field=models.FloatField(verbose_name='Application rate(mm/hr)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='end_time',
            field=models.TimeField(verbose_name='End time', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='flume_location',
            field=models.CharField(max_length=30, verbose_name='Flume location', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='furrow_irr_time',
            field=models.FloatField(verbose_name='Time to irrigate one furrow (mins)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='nfurrorws_irrigated_once',
            field=models.FloatField(verbose_name='Number of furrow irrigated at once', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='quantification_method',
            field=models.CharField(max_length=30, verbose_name='Quantification method', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='start_time',
            field=models.TimeField(verbose_name='Start time', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='total_time',
            field=models.FloatField(verbose_name='Total time(mins)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='waterlevel1',
            field=models.FloatField(verbose_name='Water level 1', blank=True, null=True),
        ),
    ]
