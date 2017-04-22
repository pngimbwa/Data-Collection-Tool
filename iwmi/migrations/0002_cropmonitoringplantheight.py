# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropMonitoringPlantHeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Monitoring Date')),
                ('crop_stage', models.CharField(verbose_name='Crop Stage', max_length=50)),
                ('number_of_good_plants_row1', models.IntegerField(verbose_name='Number of good plants row1')),
                ('number_of_good_plants_row2', models.IntegerField(verbose_name='Number of good plants row2')),
                ('number_of_good_plants_row3', models.IntegerField(verbose_name='Number of good plants row3')),
                ('number_of_bad_plants_row1', models.IntegerField(verbose_name='Number of bad plants row1')),
                ('number_of_bad_plants_row2', models.IntegerField(verbose_name='Number of bad plants row2')),
                ('number_of_bad_plants_row3', models.IntegerField(verbose_name='Number of bad plants row3')),
                ('sp1_pd', models.FloatField(verbose_name='Plant density sub-plot/bed1(sq.m)')),
                ('sp2_pd', models.FloatField(verbose_name='Plant density sub-plot/bed2(sq.m)')),
                ('sp3_pd', models.FloatField(verbose_name='Plant density sub-plot/bed3(sq.m)')),
                ('sp4_pd', models.FloatField(verbose_name='Plant density sub-plot/bed4(sq.m)')),
                ('sp5_pd', models.FloatField(verbose_name='Plant density sub-plot/bed5(sq.m)')),
                ('lenght_of_crop_stage', models.FloatField(verbose_name='Lenght of crop stage(days)')),
                ('row1_plant_height1', models.FloatField(verbose_name='Row1 Plant height1(m)')),
                ('row1_plant_height2', models.FloatField(verbose_name='Row1 Plant height2(m)')),
                ('row1_plant_height3', models.FloatField(verbose_name='Row1 Plant height3(m)')),
                ('row2_plant_height1', models.FloatField(verbose_name='Row2 Plant height1(m)')),
                ('row2_plant_height2', models.FloatField(verbose_name='Row2 Plant height2(m)')),
                ('row2_plant_height3', models.FloatField(verbose_name='Row2 Plant height3(m)')),
                ('row3_plant_height1', models.FloatField(verbose_name='Row3 Plant height1(m)')),
                ('row3_plant_height2', models.FloatField(verbose_name='Row3 Plant height2(m)')),
                ('row3_plant_height3', models.FloatField(verbose_name='Row3 Plant height3(m)')),
                ('row4_plant_height1', models.FloatField(verbose_name='Row4 Plant height1(m)')),
                ('row4_plant_height2', models.FloatField(verbose_name='Row4 Plant height2(m)')),
                ('row4_plant_height3', models.FloatField(verbose_name='Row4 Plant height3(m)')),
                ('row5_plant_height1', models.FloatField(verbose_name='Row5 Plant height1(m)')),
                ('row5_plant_height2', models.FloatField(verbose_name='Row5 Plant height2(m)')),
                ('row5_plant_height3', models.FloatField(verbose_name='Row5 Plant height3(m)')),
                ('row1_plant_Canopy_width1', models.FloatField(verbose_name='Row1 plant Canopy width1(m)')),
                ('row1_plant_Canopy_width2', models.FloatField(verbose_name='Row1 plant Canopy width2(m)')),
                ('row1_plant_Canopy_width3', models.FloatField(verbose_name='Row1 plant Canopy width3(m)')),
                ('row2_plant_Canopy_width1', models.FloatField(verbose_name='Row2 plant Canopy width1(m)')),
                ('row2_plant_Canopy_width2', models.FloatField(verbose_name='Row2 plant Canopy width2(m)')),
                ('row3_plant_Canopy_width1', models.FloatField(verbose_name='Row3 plant Canopy width1(m)')),
                ('row3_plant_Canopy_width2', models.FloatField(verbose_name='Row3 plant_Canopy_width2(m)')),
                ('row3_plant_Canopy_width3', models.FloatField(verbose_name='Row3 plant Canopy width3(m)')),
                ('sp1_numberleaves1', models.IntegerField(verbose_name='SP1_Numberleaves1')),
                ('sp1_numberleaves2', models.IntegerField(verbose_name='SP1_Numberleaves2')),
                ('sp1_numberleaves3', models.IntegerField(verbose_name='SP1_Numberleaves3')),
                ('sp2_numberleaves1', models.IntegerField(verbose_name='SP2_Numberleaves1')),
                ('sp2_numberleaves2', models.IntegerField(verbose_name='SP2_Numberleaves2')),
                ('sp2_numberleaves3', models.IntegerField(verbose_name='SP2_Numberleaves3')),
                ('sp3_numberleaves1', models.IntegerField(verbose_name='SP3_Numberleaves1')),
                ('sp3_numberleaves2', models.IntegerField(verbose_name='SP3_Numberleaves2')),
                ('sp3_numberleaves3', models.IntegerField(verbose_name='SP3_Numberleaves3')),
                ('sp4_numberleaves1', models.IntegerField(verbose_name='SP4_Numberleaves1')),
                ('sp4_numberleaves2', models.IntegerField(verbose_name='SP4_Numberleaves2')),
                ('sp4_numberleaves3', models.IntegerField(verbose_name='SP4_Numberleaves3')),
                ('sp5_numberleaves1', models.IntegerField(verbose_name='SP5_Numberleaves1')),
                ('sp5_numberleaves2', models.IntegerField(verbose_name='SP5_Numberleaves2')),
                ('sp5_numberleaves3', models.IntegerField(verbose_name='SP5_Numberleaves3')),
                ('sp1_leavelength1', models.FloatField(verbose_name='SP1_Leavelength1(cm)')),
                ('sp1_leavelength2', models.FloatField(verbose_name='SP1_Leavelength2(cm)')),
                ('sp1_leavelength3', models.FloatField(verbose_name='SP1_Leavelength3(cm)')),
                ('sp2_leavelength1', models.FloatField(verbose_name='SP2_Leavelength1(cm)')),
                ('sp2_leavelength2', models.FloatField(verbose_name='SP2_Leavelength2(cm)')),
                ('sp2_leavelength3', models.FloatField(verbose_name='SP2_Leavelength3(cm)')),
                ('sp3_leavelength1', models.FloatField(verbose_name='SP3_Leavelength1(cm)')),
                ('sp3_leavelength2', models.FloatField(verbose_name='SP3_Leavelength2(cm)')),
                ('sp3_leavelength3', models.FloatField(verbose_name='SP3_Leavelength3(cm)')),
                ('sp4_leavelength1', models.FloatField(verbose_name='SP4_Leavelength1(cm)')),
                ('sp4_leavelength2', models.FloatField(verbose_name='SP4_Leavelength2(cm)')),
                ('sp4_leavelength3', models.FloatField(verbose_name='SP4_Leavelength3(cm)')),
                ('sp5_leavelength1', models.FloatField(verbose_name='SP5_Leavelength1(cm)')),
                ('sp5_leavelength2', models.FloatField(verbose_name='SP5_Leavelength2(cm)')),
                ('sp5_leavelength3', models.FloatField(verbose_name='SP5_Leavelength3(cm)')),
                ('sp1_leavewidth1', models.FloatField(verbose_name='SP1_Leavelength1(cm)')),
                ('sp1_leavewidth2', models.FloatField(verbose_name='SP1_Leavelength2(cm)')),
                ('sp1_leavewidth3', models.FloatField(verbose_name='SP1_Leavelength3(cm)')),
                ('sp2_leavewidth1', models.FloatField(verbose_name='SP2_Leavelength1(cm)')),
                ('sp2_leavewidth2', models.FloatField(verbose_name='SP2_Leavelength2(cm)')),
                ('sp2_leavewidth3', models.FloatField(verbose_name='SP2_Leavelength3(cm)')),
                ('sp3_leavewidth1', models.FloatField(verbose_name='SP3_Leavelength1(cm)')),
                ('sp3_leavewidth2', models.FloatField(verbose_name='SP3_Leavelength2(cm)')),
                ('sp3_leavewidth3', models.FloatField(verbose_name='SP3_Leavelength3(cm)')),
                ('sp4_leavewidth1', models.FloatField(verbose_name='SP4_Leavelength1(cm)')),
                ('sp4_leavewidth2', models.FloatField(verbose_name='SP4_Leavelength2(cm)')),
                ('sp4_leavewidth3', models.FloatField(verbose_name='SP4_Leavelength3(cm)')),
                ('sp5_leavewidth1', models.FloatField(verbose_name='SP5_Leavelength1(cm)')),
                ('sp5_leavewidth2', models.FloatField(verbose_name='SP5_Leavelength2(cm)')),
                ('sp5_leavewidth3', models.FloatField(verbose_name='SP5_Leavelength3(cm)')),
                ('sp1_lai', models.FloatField(verbose_name='Calculated LAI 1')),
                ('sp2_lai', models.FloatField(verbose_name='Calculated LAI 2')),
                ('sp3_lai', models.FloatField(verbose_name='Calculated LAI 3')),
                ('sp4_lv', models.FloatField(verbose_name='Calculated LAI 4')),
                ('sp5_lai', models.FloatField(verbose_name='Calculated LAI 5')),
                ('av_lai', models.FloatField(verbose_name='Average LAI')),
                ('stdev_lai', models.FloatField(verbose_name='Stdev LAI')),
                ('visual_lai', models.FloatField(verbose_name='VisualLAI')),
                ('farm', models.ForeignKey(verbose_name='Farm', to='iwmi.Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
