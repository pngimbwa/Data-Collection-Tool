# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedNursery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('area', models.FloatField(verbose_name='Area (sq.m)')),
                ('numbers', models.IntegerField(verbose_name='Numbers of bed(s)')),
                ('planting_density_per_bed', models.FloatField(verbose_name='Planting density per bed')),
                ('seedrate', models.FloatField(verbose_name='Seed rate (kg/ha)')),
                ('seedling_yield_per_bed', models.FloatField(verbose_name='Seedling yield per bed')),
            ],
            options={
                'ordering': ['nursery'],
            },
        ),
        migrations.CreateModel(
            name='BedPlot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('numbers', models.IntegerField(verbose_name='Number of beds')),
                ('planting_density', models.IntegerField(verbose_name='Planting density')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='ConsumedCrop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Sell date')),
                ('amount', models.FloatField(verbose_name='Consumed amount')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('name', models.CharField(serialize=False, max_length=20, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CropMonitoringPlantHeight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Monitoring Date')),
                ('crop_stage', models.CharField(max_length=50, verbose_name='Crop Stage')),
                ('plant_density_per_bed', models.FloatField(null=True, verbose_name='Plant density/bed', blank=True)),
                ('plant_density_per_sqm', models.FloatField(null=True, verbose_name='plant density/sq.m', blank=True)),
                ('number_of_good_plants', models.IntegerField(null=True, verbose_name='Number of good plants', blank=True)),
                ('number_of_bad_plants', models.IntegerField(null=True, verbose_name='Number of bad plants', blank=True)),
                ('plant_number', models.IntegerField(null=True, verbose_name='Number of bad plants', blank=True)),
                ('plant_height', models.FloatField(null=True, verbose_name='Plant height(m)', blank=True)),
                ('plant_canopy_width', models.FloatField(null=True, verbose_name='Plant canopy width(m)', blank=True)),
                ('length_of_crop_stage', models.FloatField(null=True, verbose_name='Length of crop stage(days)', blank=True)),
                ('plant_leave_number', models.IntegerField(null=True, verbose_name='Leaves per plant', blank=True)),
                ('plant_leave_length', models.FloatField(null=True, verbose_name='Plant leave length(cm)', blank=True)),
                ('plant_leave_width', models.FloatField(null=True, verbose_name='Plant leave width(cm)', blank=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='CropPropertyNursery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('root_depth', models.FloatField(verbose_name='Root depth (m)')),
                ('planting_spacing', models.FloatField()),
                ('name', models.ForeignKey(verbose_name='Crop', to='iwmiproject.Crop')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='district')),
            ],
            options={
                'ordering': ['district'],
            },
        ),
        migrations.CreateModel(
            name='FarmCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('year', models.IntegerField(verbose_name='Year')),
                ('landpreparation', models.FloatField(verbose_name='Land preparation cost (Tsh)')),
                ('landpulverization', models.FloatField(verbose_name='land pulverization cost (Tsh)')),
                ('transplanting', models.FloatField(verbose_name='Transplanting cost (Tsh)')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='FarmGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('name', models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FertilizerManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Application Date')),
                ('crop_stage', models.CharField(max_length=40, verbose_name='Crop Stage')),
                ('quantity_in_kg', models.FloatField(null=True, verbose_name='Quantity(Kg)', blank=True)),
                ('fertilizer_management', models.CharField(max_length=75, verbose_name='Fertilizer Management')),
                ('nitrogen', models.FloatField(verbose_name='N content (%)')),
                ('phosphorus', models.FloatField(verbose_name='Phosphorus (ppm)')),
                ('potassium', models.FloatField(verbose_name='Potassium (ppm)')),
                ('sulphur', models.FloatField(null=True, verbose_name='Sulphur(g/kg)', blank=True)),
                ('organic_matter', models.FloatField(verbose_name='Organic Matter (%)')),
                ('price', models.FloatField(null=True, verbose_name='Price', blank=True)),
                ('price_unit', models.FloatField(null=True, verbose_name='Price Unit', blank=True)),
                ('fertilizer', models.ForeignKey(verbose_name='Fertilizer', to='iwmiproject.Fertilizer')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('name', models.CharField(serialize=False, max_length=35, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FuelManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date of use')),
                ('initial_time', models.TimeField(verbose_name='Initial Time')),
                ('final_time', models.TimeField(verbose_name='Final Time')),
                ('amount_used', models.FloatField(verbose_name='Amount Used (Litre)')),
                ('refilled_amount', models.FloatField(verbose_name='Refilled amount (Litre)')),
                ('fuel', models.ForeignKey(verbose_name='Fuel', to='iwmiproject.Fuel')),
            ],
            options={
                'ordering': ['fuel'],
            },
        ),
        migrations.CreateModel(
            name='Furrow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('numbers', models.IntegerField(verbose_name='Number of furrows')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='GravimetricSoilMoisture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('time', models.TimeField(null=True, verbose_name='Time taken', blank=True)),
                ('depth', models.FloatField(null=True, verbose_name='Depth sample', blank=True)),
                ('volume_core_used', models.FloatField(null=True, verbose_name='Volume core used (cm3)', blank=True)),
                ('weight_core_used', models.FloatField(null=True, verbose_name='Weight core used (g)', blank=True)),
                ('wet_weight', models.FloatField(null=True, verbose_name='Wet weight (g)', blank=True)),
                ('dry_weight', models.FloatField(null=True, verbose_name='Dry weight(g)', blank=True)),
                ('bulk_density', models.FloatField(null=True, verbose_name='Bulk density(g/cm3)', blank=True)),
                ('gravimetric_moisture_content', models.FloatField(null=True, verbose_name='Gravimetric moisture content', blank=True)),
                ('volumetric_moisture_content', models.FloatField(null=True, verbose_name='Volumetric moisture content', blank=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Harvest date')),
                ('time', models.FloatField(verbose_name='Time taken')),
                ('amount', models.FloatField(verbose_name='Harvest amount')),
                ('amount_for_home', models.FloatField(verbose_name='Harvest amount for home(Kg)')),
                ('amount_for_sell', models.FloatField(verbose_name='Harvest amount for sell(Kg)')),
                ('crop', models.ForeignKey(verbose_name='Harvested crop', to='iwmiproject.Crop')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
        migrations.CreateModel(
            name='LabourManagament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('labour', models.CharField(max_length=35, verbose_name='Labour')),
                ('hired_female_number', models.IntegerField(verbose_name='Numbe of hired female labour')),
                ('hired_male_number', models.IntegerField(verbose_name='Number of hired male labour')),
                ('family_female_number', models.IntegerField(verbose_name='Number of family female labour')),
                ('family_male_number', models.IntegerField(verbose_name='Number of family male labour')),
                ('activity', models.CharField(max_length=100, verbose_name='Performed activity')),
                ('wage', models.FloatField(verbose_name='Daily wage')),
                ('price_unit', models.CharField(default='Tsh', max_length=10, verbose_name='Currency')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='LandClearance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('landclearanceoption', models.CharField(max_length=50, verbose_name='Land clearance option')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='LandPreparation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Land preparation date')),
                ('landpreparationtool', models.CharField(max_length=50, verbose_name='Land preparation tool')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('NurseryID', models.CharField(serialize=False, max_length=25, primary_key=True, verbose_name='Nursery ID')),
                ('area', models.FloatField(verbose_name='Area(sq.m)')),
                ('date_bed_preparation', models.DateField(verbose_name='Bed Preparation date')),
                ('date_trasplanting', models.DateField(verbose_name='Transplanting date')),
            ],
            options={
                'ordering': ['NurseryID'],
            },
        ),
        migrations.CreateModel(
            name='NurseryIrrigationEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Irrigation Date')),
                ('time_started', models.TimeField(verbose_name='Time started')),
                ('time_ended', models.TimeField(verbose_name='Time ended')),
                ('total_time', models.FloatField(verbose_name='Total time(minutes)')),
                ('event', models.IntegerField(verbose_name='Event number')),
                ('discharge', models.FloatField(verbose_name='Discharge(m3/s)')),
                ('standard_volume', models.FloatField(verbose_name='Standard Volume (Litre or m3/s)')),
                ('quantity', models.FloatField(null=True, verbose_name='Quantity', blank=True)),
                ('climate', models.CharField(max_length=30, verbose_name='Climate')),
                ('total_volume', models.FloatField(verbose_name='Total Volume (Litre)')),
                ('nursery', models.ForeignKey(verbose_name='Nursery', to='iwmiproject.Nursery')),
            ],
            options={
                'ordering': ['nursery'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('personID', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='Person ID')),
                ('firstname', models.CharField(max_length=80, verbose_name='First name')),
                ('middlename', models.CharField(null=True, max_length=80, verbose_name='Middle name', blank=True)),
                ('lastname', models.CharField(max_length=80, verbose_name='Last name')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('role', models.CharField(max_length=40, verbose_name='Role')),
                ('phone', models.CharField(null=True, max_length=50, verbose_name='Phone', blank=True)),
            ],
            options={
                'ordering': ['personID'],
            },
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('name', models.CharField(serialize=False, max_length=85, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PesticideManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Application Date')),
                ('crop_stage', models.CharField(max_length=40, verbose_name='Crop Stage')),
                ('form', models.CharField(max_length=20, verbose_name='Form')),
                ('quantity_in_litre', models.FloatField(null=True, verbose_name='Quantity(Litre)', blank=True)),
                ('quantity_in_kg', models.FloatField(null=True, verbose_name='Quantity(Kg)', blank=True)),
                ('price', models.FloatField(null=True, verbose_name='Price', blank=True)),
                ('price_unit', models.FloatField(null=True, verbose_name='Price Unit', blank=True)),
                ('name', models.ForeignKey(verbose_name='Name', to='iwmiproject.Pesticide')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PlantingMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('planting_method', models.CharField(max_length=100, verbose_name='Planting Method')),
                ('seeding_date', models.DateField(null=True, verbose_name='Seeding Date', blank=True)),
                ('planting_date', models.DateField(null=True, verbose_name='Planting date', blank=True)),
                ('seeding_rate', models.FloatField(null=True, verbose_name='seeding rate', blank=True)),
                ('seed_spacing_within_a_row', models.FloatField(null=True, verbose_name='seed spacing within a row(cm)', blank=True)),
                ('seed_spacing_btn_a_row', models.FloatField(null=True, verbose_name='seed spacing btn a row(cm)', blank=True)),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('plotID', models.CharField(max_length=50, verbose_name='PlotID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='PlotCropProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('root_depth', models.FloatField(verbose_name='Root depth (m)')),
                ('planting_spacing', models.FloatField(verbose_name='Planting space(cm)')),
                ('name', models.ForeignKey(verbose_name='Crop', to='iwmiproject.Crop')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='Plot ID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='PlotCultivation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Cultivation date')),
                ('cultivation_method', models.CharField(max_length=80, verbose_name='Method of Cultivation')),
                ('plotID', models.ForeignKey(verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='PlotIrrigationEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('irrigation_event', models.IntegerField(verbose_name='Irrigation Event')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time(mins)')),
                ('quantification_method', models.CharField(max_length=30, verbose_name='Quantification method')),
                ('flume_location', models.CharField(max_length=30, verbose_name='Flume location')),
                ('waterlevel1', models.FloatField(verbose_name='Water level 1')),
                ('waterlevel2', models.FloatField(null=True, verbose_name='Water level 2', blank=True)),
                ('furrow_irr_time', models.FloatField(verbose_name='Time to irrigate one furrow (mins)')),
                ('nfurrorws_irrigated_once', models.FloatField(verbose_name='Number of furrow irrigated at once')),
                ('application_rate', models.FloatField(null=True, verbose_name='Application rate(m3/s)', blank=True)),
                ('standardvolume', models.FloatField(null=True, verbose_name='Standard volume', blank=True)),
                ('quantity_of_units', models.IntegerField(null=True, verbose_name='Quantity of unit', blank=True)),
                ('yellow_WFD_before_irrigation', models.IntegerField(null=True, verbose_name='Yellow WFD before irrigation', blank=True)),
                ('red_WFD_before_irrigation', models.IntegerField(null=True, verbose_name='Red WFD before irrigation', blank=True)),
                ('yellow_WFD_time_after_irrigation', models.FloatField(null=True, verbose_name='Yellow WFD time after irrigation', blank=True)),
                ('red_WFD_time_after_irrigation', models.FloatField(null=True, verbose_name='Red WFD time after irrigation', blank=True)),
                ('climate', models.CharField(max_length=20, verbose_name='Climate')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='PlotManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('elevation', models.FloatField(null=True, verbose_name='elevation', blank=True)),
                ('plot_size', models.FloatField(verbose_name='Plot size(sq.m)')),
                ('water_management_method', models.CharField(max_length=80, verbose_name='Water management method')),
                ('water_source', models.CharField(max_length=80, verbose_name='Water Source')),
                ('water_application', models.CharField(max_length=80, verbose_name='Water Application')),
                ('crop', models.ForeignKey(verbose_name='Crop', to='iwmiproject.Crop')),
                ('plotID', models.ForeignKey(verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='PlotOperation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date activity was performed')),
                ('activity', models.TextField(max_length=200, verbose_name='Activity')),
                ('number', models.IntegerField(verbose_name='Number of people')),
                ('plotID', models.ForeignKey(verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('name', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PumpingSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='date')),
                ('source', models.CharField(max_length=80, verbose_name='Name')),
                ('latitude', models.FloatField(verbose_name="Source's latitude")),
                ('longitude', models.FloatField(verbose_name="Source's longitude")),
                ('depth', models.FloatField(null=True, verbose_name='Depth(m)', blank=True)),
                ('diameter', models.FloatField(null=True, verbose_name='Diameter(m)', blank=True)),
            ],
            options={
                'ordering': ['depth'],
            },
        ),
        migrations.CreateModel(
            name='PumpOwnership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('size', models.CharField(max_length=50, verbose_name='size')),
                ('price', models.FloatField(null=True, verbose_name='Bought price', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Bought date', blank=True)),
                ('group', models.ForeignKey(verbose_name='FarmGroup', to='iwmiproject.FarmGroup')),
                ('name', models.ForeignKey(null=True, blank=True, verbose_name='Name', to='iwmiproject.Pump')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='region')),
                ('country', models.ForeignKey(verbose_name='country', to='iwmiproject.Country')),
            ],
            options={
                'ordering': ['region'],
            },
        ),
        migrations.CreateModel(
            name='RelationManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('farmer', models.CharField(max_length=25, verbose_name='farmer')),
                ('relation', models.CharField(max_length=20, verbose_name='Relation')),
            ],
            options={
                'ordering': ['farmer'],
            },
        ),
        migrations.CreateModel(
            name='ResidueManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('time_taken', models.FloatField(verbose_name='Time taken')),
                ('burnt', models.BooleanField(default=False, verbose_name='Burnt')),
                ('livestock', models.BooleanField(default=False, verbose_name='Used for livestock')),
                ('purpose', models.TextField(max_length=100, verbose_name='Purpose')),
                ('crop', models.ForeignKey(verbose_name='crop', to='iwmiproject.Crop')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='SaleHarvestedCrop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Selling date')),
                ('amount', models.FloatField(verbose_name='Amount sold')),
                ('income', models.FloatField(verbose_name='Total income (Tsh)')),
                ('expenditure', models.FloatField(verbose_name='Expenditure (Tsh)')),
                ('net_income', models.FloatField(verbose_name='Net income (Tsh)')),
                ('crop', models.ForeignKey(verbose_name='crop', to='iwmiproject.Crop')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('name', models.CharField(serialize=False, max_length=35, primary_key=True, verbose_name='Seed')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SeedManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('quantity', models.FloatField(verbose_name='Quantity (kg)')),
                ('price_per_unit', models.FloatField(verbose_name='Price per unit (Tsh)')),
                ('total_cost', models.FloatField(verbose_name='Total cost (Tsh)')),
                ('nursery', models.ForeignKey(verbose_name='Nursery planted on', to='iwmiproject.Nursery')),
                ('seed', models.ForeignKey(verbose_name='Seed', to='iwmiproject.Seed')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='date')),
                ('repaire_type', models.TextField(max_length=100, verbose_name='Type of repaires')),
                ('price', models.FloatField(verbose_name='Price of spaire parts (Tsh)')),
                ('total_cost', models.FloatField(verbose_name='Total repaire cost (Tsh)')),
                ('group', models.ForeignKey(verbose_name='FarmGroup', to='iwmiproject.FarmGroup')),
                ('pump', models.ManyToManyField(to='iwmiproject.Pump', verbose_name='Pump')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('name', models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SoilMoistureMeasurementManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement_option', models.CharField(max_length=75, verbose_name='Soil measurement used(option)')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='SoilMoistureProfiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement', models.IntegerField(null=True, verbose_name='Measurement number', blank=True)),
                ('depth_10', models.FloatField(null=True, verbose_name='Measurement at 10cm', blank=True)),
                ('depth_20', models.FloatField(null=True, verbose_name='VMeasurement at 20cm', blank=True)),
                ('depth_30', models.FloatField(null=True, verbose_name='Measurement at 30cm', blank=True)),
                ('depth_40', models.FloatField(null=True, verbose_name='Measurement at 40cm', blank=True)),
                ('depth_60', models.FloatField(null=True, verbose_name='Measurement at 60cm', blank=True)),
                ('depth_100', models.FloatField(null=True, verbose_name='Measurement at 100cm', blank=True)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='SoilProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('pH', models.FloatField(null=True, verbose_name='pH', blank=True)),
                ('ec', models.FloatField(null=True, verbose_name='Electrical conductivity (dS/m)', blank=True)),
                ('sand', models.FloatField(null=True, verbose_name='Sand (%)', blank=True)),
                ('clay', models.FloatField(null=True, verbose_name='Clay(%)', blank=True)),
                ('silt', models.FloatField(null=True, verbose_name='Silt(%)', blank=True)),
                ('cec', models.FloatField(null=True, verbose_name='CEC', blank=True)),
                ('om', models.FloatField(null=True, verbose_name='OM(%)', blank=True)),
                ('tn', models.FloatField(null=True, verbose_name='TN(%)', blank=True)),
                ('av_p', models.FloatField(null=True, verbose_name='Av.p (ppm)', blank=True)),
                ('fe', models.FloatField(null=True, verbose_name='Fe (ppm)', blank=True)),
                ('fc', models.FloatField(null=True, verbose_name='Fe (ppm)', blank=True)),
                ('pwp', models.FloatField(null=True, verbose_name='pwp(%)', blank=True)),
                ('k', models.FloatField(null=True, verbose_name='K(cmol/kg)', blank=True)),
                ('bulkdensity', models.FloatField(null=True, verbose_name='bulk density (g/cm3)', blank=True)),
                ('zn', models.FloatField(null=True, verbose_name='Zn(g/kg)', blank=True)),
                ('se', models.FloatField(null=True, verbose_name='Se(g/kg)', blank=True)),
                ('ca', models.FloatField(null=True, verbose_name='Ca(g/kg)', blank=True)),
                ('s', models.FloatField(null=True, verbose_name='S(g/kg)', blank=True)),
                ('mg', models.FloatField(null=True, verbose_name='Mg(g/kg)', blank=True)),
                ('na', models.FloatField(null=True, verbose_name='Na(g/kg)', blank=True)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
                ('soilclass', models.ForeignKey(verbose_name='Soil class', to='iwmiproject.Soil')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Spaire',
            fields=[
                ('name', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='name')),
                ('pump', models.ManyToManyField(to='iwmiproject.Pump', verbose_name='Pump')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SpaireManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('price', models.FloatField(null=True, verbose_name='Bought price (Tsh)', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Bought date', blank=True)),
                ('group', models.ForeignKey(verbose_name='FarmGroup', to='iwmiproject.FarmGroup')),
                ('spaire', models.ForeignKey(verbose_name='Spaire', to='iwmiproject.Spaire')),
            ],
            options={
                'ordering': ['group'],
            },
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, related_name='custom_user_profile', to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=80, verbose_name='First name')),
                ('middlename', models.CharField(null=True, max_length=80, verbose_name='Middle name', blank=True)),
                ('lastname', models.CharField(max_length=80, verbose_name='Last name')),
                ('role', models.CharField(max_length=40, verbose_name='Role')),
                ('phone', models.CharField(null=True, max_length=50, verbose_name='Phone', blank=True)),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('institution', models.CharField(max_length=100, verbose_name='Institution')),
                ('country', models.ForeignKey(verbose_name='Country', to='iwmiproject.Country')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='TDRMeasurement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement', models.FloatField(verbose_name='Measurement(%)')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name', models.CharField(serialize=False, max_length=100, primary_key=True, verbose_name='Technology')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyCalibration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Calibration Date')),
                ('repetition', models.IntegerField(verbose_name='Repetition')),
                ('bucketvolume', models.FloatField(null=True, verbose_name='Bucket volume (litre)', blank=True)),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time')),
                ('discharge', models.FloatField(null=True, verbose_name='Discharge(m3/s)', blank=True)),
                ('technology', models.ForeignKey(verbose_name='Calibrated Technology', to='iwmiproject.Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyFailure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Failure date')),
                ('reason', models.TextField(max_length=100, verbose_name='Reason')),
                ('technology', models.ForeignKey(verbose_name='Technology', to='iwmiproject.Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Received date')),
                ('technology', models.ForeignKey(verbose_name='Technology', to='iwmiproject.Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TissueNutrientAnalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('plant_tissue_part', models.CharField(max_length=30, verbose_name='Plant tissue part')),
                ('plantnumber', models.IntegerField(verbose_name='Plant number')),
                ('freshweight', models.FloatField(verbose_name='Fresh weight(kg)')),
                ('dryweight', models.FloatField(verbose_name='Dry weight(kg)')),
                ('n', models.FloatField(verbose_name='Nitrogen(%)')),
                ('p', models.FloatField(verbose_name='Phosphorus(%)')),
                ('k', models.FloatField(verbose_name='Potassium(%)')),
                ('s', models.FloatField(verbose_name='Sulphur(%)')),
                ('mg', models.FloatField(verbose_name='Magnesium(%)')),
                ('ca', models.FloatField(verbose_name='Calcium(%)')),
                ('fe', models.FloatField(verbose_name='Iron(%)')),
                ('zn', models.FloatField(verbose_name='Zinc(%)')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Transplanting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='transplanting date')),
                ('plantsnumber', models.IntegerField(verbose_name='Total number of plants transplanted')),
                ('plant_spacing_btn_row', models.FloatField(verbose_name='Plant spacing between row(cm)')),
                ('plant_spacing_btn_plants_within_rows', models.FloatField(verbose_name='Plant spacing between plants within rows(cm)')),
                ('plantsnumber_per_row', models.IntegerField(verbose_name='Plant number per row')),
                ('nurseryID', models.ForeignKey(null=True, blank=True, verbose_name='nurseryID', to='iwmiproject.Nursery')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('village', models.CharField(serialize=False, max_length=45, primary_key=True, verbose_name='village')),
                ('district', models.ForeignKey(verbose_name='district', to='iwmiproject.District')),
            ],
            options={
                'ordering': ['village'],
            },
        ),
        migrations.CreateModel(
            name='WaterSourceCategory',
            fields=[
                ('category', models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Pumping Source')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='WaterSources',
            fields=[
                ('ID', models.CharField(serialize=False, max_length=10, primary_key=True, verbose_name='Water source ID')),
                ('name', models.CharField(max_length=50, verbose_name='Water source type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Weed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Weeding date')),
                ('weed_activities', models.CharField(max_length=100, verbose_name='What they do')),
                ('time', models.FloatField(verbose_name='Time taken')),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='YieldFarmLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Harvesting Date')),
                ('area', models.FloatField(verbose_name='Area (sq.m)')),
                ('fresh_dry', models.CharField(null=True, max_length=10, verbose_name='Fresh/Dry', blank=True)),
                ('marketable_yield', models.FloatField(verbose_name='Marketable yield (Kg)')),
                ('unmarketable_yield', models.FloatField(verbose_name='Unmarketable yield (Kg)')),
                ('biomas', models.FloatField(verbose_name='Biomas (Kg)')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='YieldPlantLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('harvest_method', models.CharField(max_length=50, verbose_name='Harvest Method')),
                ('fresh_dry', models.CharField(max_length=10, verbose_name='Fresh/Dry')),
                ('plant_number', models.IntegerField(null=True, verbose_name='Plant number', blank=True)),
                ('marketable_produced', models.FloatField(null=True, verbose_name='Number of marketable produced', blank=True)),
                ('unmarketable_produced', models.FloatField(null=True, verbose_name='Number of unmarketable produced', blank=True)),
                ('marketable_produced_weight', models.FloatField(null=True, verbose_name='Total weight of marketable produced(kg)', blank=True)),
                ('unmarketable_produced_weight', models.FloatField(null=True, verbose_name=' Total weight of unmarketable produced(kg)', blank=True)),
                ('diameter_width_produced', models.FloatField(null=True, verbose_name='Diameter/width produce', blank=True)),
                ('length', models.FloatField(null=True, verbose_name='Length produced(cm)', blank=True)),
                ('residual_biomass', models.FloatField(null=True, verbose_name='Residual biomass(Kg)', blank=True)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='YieldRowBedLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField(verbose_name='Harvesting Date')),
                ('harvesting_method', models.CharField(max_length=80, verbose_name='Harvesting method')),
                ('fresh_dry', models.CharField(null=True, max_length=10, verbose_name='Fresh/Dry', blank=True)),
                ('area', models.FloatField(null=True, verbose_name='area(sq.m)', blank=True)),
                ('marketable_produced', models.FloatField(null=True, verbose_name='Marketable produced', blank=True)),
                ('ummarketable_produced', models.FloatField(null=True, verbose_name='Unmarketable produced', blank=True)),
                ('marketable_produced_weight', models.FloatField(null=True, verbose_name='Weight of marketable produced(kg)', blank=True)),
                ('unmarketable_produced_weight', models.FloatField(null=True, verbose_name=' Weight of unmarketable produced(kg)', blank=True)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('farmID', models.OneToOneField(serialize=False, primary_key=True, related_name='farms', to='iwmiproject.People')),
                ('number', models.IntegerField(verbose_name='Total plot numbers')),
                ('fieldsize', models.FloatField(verbose_name='Field Size (sq.m)')),
                ('total_irrigated_plots_land_area', models.FloatField(verbose_name='Total irrigated plots land area (sq.m)')),
                ('total_irrigated_plots', models.IntegerField(verbose_name='Number of irrigated plots')),
            ],
            options={
                'ordering': ['farmID'],
            },
        ),
        migrations.AddField(
            model_name='watersourcecategory',
            name='watersourcetype',
            field=models.ForeignKey(verbose_name='Water source type', to='iwmiproject.WaterSources'),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='village',
            field=models.ForeignKey(verbose_name='Village', to='iwmiproject.Village'),
        ),
        migrations.AddField(
            model_name='service',
            name='spaire',
            field=models.ManyToManyField(to='iwmiproject.Spaire', verbose_name='Required spaire'),
        ),
        migrations.AddField(
            model_name='relationmanager',
            name='family_member',
            field=models.ManyToManyField(to='iwmiproject.People', verbose_name='Household family members'),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='technology',
            field=models.ForeignKey(verbose_name='Technology', to='iwmiproject.Technology'),
        ),
        migrations.AddField(
            model_name='plot',
            name='village',
            field=models.ForeignKey(verbose_name='Village', to='iwmiproject.Village'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Plot ID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='people',
            name='group',
            field=models.ForeignKey(null=True, blank=True, verbose_name='FarmGroup', to='iwmiproject.FarmGroup'),
        ),
        migrations.AddField(
            model_name='people',
            name='village',
            field=models.ForeignKey(verbose_name='Village', to='iwmiproject.Village'),
        ),
        migrations.AddField(
            model_name='nursery',
            name='seed',
            field=models.ForeignKey(verbose_name='seed', to='iwmiproject.Seed'),
        ),
        migrations.AddField(
            model_name='nursery',
            name='technology',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Calibrated Technology', to='iwmiproject.Technology'),
        ),
        migrations.AddField(
            model_name='landpreparation',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='landclearance',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(verbose_name='Owner(Farmer)', to='iwmiproject.People'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Harvested farm', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='furrow',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Plot ID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Plot ID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='farmgroup',
            name='village',
            field=models.ForeignKey(verbose_name='Village', to='iwmiproject.Village'),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(verbose_name='region', to='iwmiproject.Region'),
        ),
        migrations.AddField(
            model_name='croppropertynursery',
            name='nursery',
            field=models.ForeignKey(verbose_name='Nursery', to='iwmiproject.Nursery'),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Plot', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='crop',
            field=models.ForeignKey(verbose_name='crop', to='iwmiproject.Crop'),
        ),
        migrations.AddField(
            model_name='bedplot',
            name='plotID',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Plot ID', to='iwmiproject.Plot'),
        ),
        migrations.AddField(
            model_name='bednursery',
            name='nursery',
            field=models.ForeignKey(verbose_name='NuseryID', to='iwmiproject.Nursery'),
        ),
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='technologymanagement',
            name='farm',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='technologyfailure',
            name='farm',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='technologycalibration',
            name='farm',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='residuemanagement',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='pumpingsource',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm(s)', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='farm',
            field=models.ForeignKey(verbose_name='FieldID', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='plot',
            name='farm',
            field=models.ForeignKey(verbose_name='FarmID', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='nursery',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AlterUniqueTogether(
            name='harvest',
            unique_together=set([('plotID', 'date')]),
        ),
        migrations.AddField(
            model_name='fuelmanagement',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AlterUniqueTogether(
            name='farmgroup',
            unique_together=set([('name', 'village')]),
        ),
        migrations.AddField(
            model_name='farmcost',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='farm',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Farm', to='iwmiproject.Farm'),
        ),
        migrations.AlterUniqueTogether(
            name='pumpingsource',
            unique_together=set([('latitude', 'longitude')]),
        ),
        migrations.AlterUniqueTogether(
            name='plot',
            unique_together=set([('farm', 'plotID')]),
        ),
    ]
