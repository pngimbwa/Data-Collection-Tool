# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0140_auto_20170126_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='Crop',
            field=models.ForeignKey(null=True, verbose_name='Crop', to='iwmiproject.Crop', blank=True),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='LAI_three',
            field=models.FloatField(null=True, blank=True, verbose_name='leaf area index (LAI)  for plant three'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='LAI_two',
            field=models.FloatField(null=True, blank=True, verbose_name='leaf area index (LAI) for plant two '),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='length_of_crop_stage_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Length of crop three stage(days)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='length_of_crop_stage_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Length of crop two stage(days)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant three canopy width(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant two canopy width(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_height_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant three height(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_height_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant two height(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_length_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant three leave length(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_length_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant two leave length(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_number_three',
            field=models.IntegerField(null=True, blank=True, verbose_name='Leaves per plant three'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_number_two',
            field=models.IntegerField(null=True, blank=True, verbose_name='Leaves per plant two'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_width_three',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant three leave width(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_width_two',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant two leave width(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_number_three',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant Number three'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='plant_number_two',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant Number two'),
        ),
    ]
