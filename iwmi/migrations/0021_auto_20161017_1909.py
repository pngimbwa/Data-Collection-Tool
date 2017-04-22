# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0020_auto_20161017_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Number')),
                ('farm', models.ManyToManyField(to='iwmi.Farm', verbose_name='Farm(s)')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='SoilMoistureProfiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement', models.IntegerField(null=True, blank=True, verbose_name='Measurement number')),
                ('depth_10', models.FloatField(null=True, blank=True, verbose_name='Measurement at 10cm')),
                ('depth_20', models.FloatField(null=True, blank=True, verbose_name='VMeasurement at 20cm')),
                ('depth_30', models.FloatField(null=True, blank=True, verbose_name='Measurement at 30cm')),
                ('depth_40', models.FloatField(null=True, blank=True, verbose_name='Measurement at 40cm')),
                ('depth_60', models.FloatField(null=True, blank=True, verbose_name='Measurement at 60cm')),
                ('depth_100', models.FloatField(null=True, blank=True, verbose_name='Measurement at 100cm')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RenameField(
            model_name='yieldplantlevel',
            old_name='dry',
            new_name='fresh_dry',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='av_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_Canopy_width1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_Canopy_width2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp1_pd',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp2_pd',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp3_pd',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_lv',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp4_pd',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves1',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves2',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves3',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='sp5_pd',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='stdev_lai',
        ),
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='visual_lai',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='Average_length',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP1Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP1Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP1Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP2Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP2Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP2Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP3Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP3Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP3Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP4Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP4Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP4Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP5Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP5Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP5Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP6Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP6Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='diam_WidthP6Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='fresh',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP1Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP1Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP1Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP2Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP2Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP2Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP3Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP3Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP3Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP4Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP4Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP4Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP5Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP5Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP5Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP6Row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP6Row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='lengthP6Row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant1row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant1row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant1row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant2row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant2row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant2row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant3row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant3row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='nmplant3row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant1row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant1row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant1row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant2row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant2row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant2row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant3row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant3row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='numplant3row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p1_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p1_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p1_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p2_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p2_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p2_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p3_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p3_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='residual_biomass_p3_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='stdev_length',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl1_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl1_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl1_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl2_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl2_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl2_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl3_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl3_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wmpl3_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl1_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl1_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl1_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl2_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl2_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl2_row3',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl3_row1',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl3_row2',
        ),
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='wumpl3_row3',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='dry',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='fresh',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='nmrow1',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='nmrow2',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='nmrow3',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='numrow1',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='numrow2',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='numrow3',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='sub_plot_area',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wmrow1',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wmrow2',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wmrow3',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wumrow1',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wumrow2',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='wumrow3',
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of bad plants'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of good plants'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_canopy_width',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant one canopy width(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_density_per_bed',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant density/bed'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_density_per_sqm',
            field=models.FloatField(null=True, blank=True, verbose_name='plant density/sq.m'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_height',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant one height(m)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_length',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave length(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_number',
            field=models.IntegerField(null=True, blank=True, verbose_name='Leaves per plant'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_leave_width',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant leave width(cm)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plant_number',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of bad plants'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='diameter_width_produced',
            field=models.FloatField(null=True, blank=True, verbose_name='Diameter/width produce'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='length',
            field=models.FloatField(null=True, blank=True, verbose_name='Length produced(cm)'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='marketable_produced',
            field=models.FloatField(null=True, blank=True, verbose_name='Number of marketable produced'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='marketable_produced_weight',
            field=models.FloatField(null=True, blank=True, verbose_name='Total weight of marketable produced(kg)'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='plant_number',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant number'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='residual_biomass',
            field=models.FloatField(null=True, blank=True, verbose_name='Residual biomass(Kg)'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='unmarketable_produced',
            field=models.FloatField(null=True, blank=True, verbose_name='Number of unmarketable produced'),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='unmarketable_produced_weight',
            field=models.FloatField(null=True, blank=True, verbose_name=' Total weight of unmarketable produced(kg)'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='area',
            field=models.FloatField(null=True, blank=True, verbose_name='area(sq.m)'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='fresh_dry',
            field=models.CharField(null=True, blank=True, verbose_name='Fresh/Dry', max_length=10),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='marketable_produced',
            field=models.FloatField(null=True, blank=True, verbose_name='Marketable produced'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='marketable_produced_weight',
            field=models.FloatField(null=True, blank=True, verbose_name='Weight of marketable produced(kg)'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='ummarketable_produced',
            field=models.FloatField(null=True, blank=True, verbose_name='Unmarketable produced'),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='unmarketable_produced_weight',
            field=models.FloatField(null=True, blank=True, verbose_name=' Weight of unmarketable produced(kg)'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='row',
            field=models.ForeignKey(to='iwmi.Row', verbose_name='Row Number', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='row',
            field=models.ForeignKey(to='iwmi.Row', verbose_name='Row number', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='row',
            field=models.ForeignKey(to='iwmi.Row', verbose_name='Row Number', null=True, blank=True),
        ),
    ]