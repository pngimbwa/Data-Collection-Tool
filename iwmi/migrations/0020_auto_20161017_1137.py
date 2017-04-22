# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0019_labour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='av_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Average LAI'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of bad plants row1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of bad plants row2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_bad_plants_row3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of bad plants row3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of good plants row1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of good plants row2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='number_of_good_plants_row3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of good plants row3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 plant Canopy width1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 plant Canopy width2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_Canopy_width3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 plant Canopy width3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 Plant height1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 Plant height2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row1_plant_height3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row1 Plant height3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_Canopy_width1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row2 plant Canopy width1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_Canopy_width2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row2 plant Canopy width2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row2 Plant height1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row2 Plant height2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row2_plant_height3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row2 Plant height3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 plant Canopy width1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 plant_Canopy_width2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_Canopy_width3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 plant Canopy width3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 Plant height1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 Plant height2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row3_plant_height3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row3 Plant height3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row4 Plant height1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row4 Plant height2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row4_plant_height3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row4 Plant height3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height1',
            field=models.FloatField(blank=True, null=True, verbose_name='Row5 Plant height1(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height2',
            field=models.FloatField(blank=True, null=True, verbose_name='Row5 Plant height2(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='row5_plant_height3',
            field=models.FloatField(blank=True, null=True, verbose_name='Row5 Plant height3(m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Calculated LAI 1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavelength3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_leavewidth3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP1_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves1',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP1_Numberleaves1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves2',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP1_Numberleaves2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_numberleaves3',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP1_Numberleaves3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp1_pd',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density sub-plot/bed1(sq.m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Calculated LAI 2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavelength3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_leavewidth3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP2_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves1',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP2_Numberleaves1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves2',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP2_Numberleaves2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_numberleaves3',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP2_Numberleaves3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp2_pd',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density sub-plot/bed2(sq.m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Calculated LAI 3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavelength3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_leavewidth3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP3_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves1',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP3_Numberleaves1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves2',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP3_Numberleaves2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_numberleaves3',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP3_Numberleaves3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp3_pd',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density sub-plot/bed3(sq.m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavelength3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_leavewidth3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP4_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_lv',
            field=models.FloatField(blank=True, null=True, verbose_name='Calculated LAI 4'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves1',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP4_Numberleaves1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves2',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP4_Numberleaves2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_numberleaves3',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP4_Numberleaves3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp4_pd',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density sub-plot/bed4(sq.m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Calculated LAI 5'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavelength3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth1',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength1(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth2',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength2(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_leavewidth3',
            field=models.FloatField(blank=True, null=True, verbose_name='SP5_Leavelength3(cm)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves1',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP5_Numberleaves1'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves2',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP5_Numberleaves2'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_numberleaves3',
            field=models.IntegerField(blank=True, null=True, verbose_name='SP5_Numberleaves3'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='sp5_pd',
            field=models.FloatField(blank=True, null=True, verbose_name='Plant density sub-plot/bed5(sq.m)'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='stdev_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='Stdev LAI'),
        ),
        migrations.AlterField(
            model_name='cropmonitoringplantheight',
            name='visual_lai',
            field=models.FloatField(blank=True, null=True, verbose_name='VisualLAI'),
        ),
    ]
