# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0139_auto_20170125_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='LAI_three',
            field=models.FloatField(null=True, blank=True, verbose_name='leaf area index (LAI) '),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='LAI_two',
            field=models.FloatField(null=True, blank=True, verbose_name='leaf area index (LAI) '),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='length_of_crop_stage_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Length of crop stage(days)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='length_of_crop_stage_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Length of crop stage(days)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant canopy width(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant canopy width(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_height_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant height(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_height_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant height(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_length_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave length(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_length_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave length(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_number_three',
            field=models.IntegerField(null=True, blank=True, verbose_name='Leaves per plant'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_number_two',
            field=models.IntegerField(null=True, blank=True, verbose_name='Leaves per plant'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_width_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave width(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_width_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave width(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_number_three',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant Number'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_number_two',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant Number'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_number',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant Number'),
        ),
    ]
