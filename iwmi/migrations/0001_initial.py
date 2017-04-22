# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedFarm',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('numbers', models.IntegerField(verbose_name='Number of beds')),
                ('planting_density', models.IntegerField(verbose_name='Planting density')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='BedNursery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
            name='ConsumedCrop',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('name', models.CharField(max_length=50, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CropPropertyFarm',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('root_depth', models.FloatField(verbose_name='Root depth (m)')),
                ('planting_spacing', models.FloatField(verbose_name='Planting space(cm)')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='CropPropertyNursery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('root_depth', models.FloatField(verbose_name='Root depth (m)')),
                ('planting_spacing', models.FloatField()),
                ('name', models.ForeignKey(to='iwmi.Crop', verbose_name='Crop')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CropVariety',
            fields=[
                ('variety', models.CharField(max_length=20, verbose_name='Variety', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['variety'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district', models.CharField(max_length=45, verbose_name='district', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['district'],
            },
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('fieldID', models.CharField(max_length=40, verbose_name='FieldID', serialize=False, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('planting_date', models.DateField(verbose_name='Planting date')),
                ('fieldsize', models.FloatField(verbose_name='Field Size (sq.m)')),
                ('water_source', models.CharField(max_length=80, verbose_name='Water Source')),
                ('water_application', models.CharField(max_length=80, verbose_name='Water Application')),
                ('pumping_source', models.CharField(max_length=80, verbose_name='Pumping source')),
                ('water_management_method', models.CharField(max_length=80, verbose_name='Water management method')),
                ('soil_moisture_method', models.CharField(max_length=45, verbose_name='Soil moisture method')),
                ('crop', models.ManyToManyField(verbose_name='Crop(s)', to='iwmi.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='FarmCost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('year', models.IntegerField(verbose_name='Year')),
                ('landpreparation', models.FloatField(verbose_name='Land preparation cost (Tsh)')),
                ('landpulverization', models.FloatField(verbose_name='land pulverization cost (Tsh)')),
                ('transplanting', models.FloatField(verbose_name='Transplanting cost (Tsh)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='FarmCultivation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Cultivation date')),
                ('cultivation_method', models.CharField(max_length=80, verbose_name='Method of Cultivation')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='FarmIrrigationEvent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('discharge', models.FloatField(null=True, verbose_name='Discharge(m3/s)', blank=True)),
                ('standardvolume', models.FloatField(null=True, verbose_name='Standard volume', blank=True)),
                ('quantity_of_units', models.IntegerField(null=True, verbose_name='Quantity of unit', blank=True)),
                ('yellow_WFD_before_irrigation', models.IntegerField(null=True, verbose_name='Yellow WFD before irrigation', blank=True)),
                ('red_WFD_before_irrigation', models.IntegerField(null=True, verbose_name='Red WFD before irrigation', blank=True)),
                ('yellow_WFD_time_after_irrigation', models.FloatField(null=True, verbose_name='Yellow WFD time after irrigation', blank=True)),
                ('red_WFD_time_after_irrigation', models.FloatField(null=True, verbose_name='Red WFD time after irrigation', blank=True)),
                ('climate', models.CharField(max_length=20, verbose_name='Climate')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='FarmOperation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date activity was performed')),
                ('activity', models.TextField(max_length=200, verbose_name='Activity')),
                ('number', models.IntegerField(verbose_name='Number of people')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FertilizerManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Application Date')),
                ('fertilizer_management', models.CharField(max_length=75, verbose_name='Fertilizer Management')),
                ('nitrogen', models.FloatField(verbose_name='N content (%)')),
                ('phosphorus', models.FloatField(verbose_name='Phosphorus (ppm)')),
                ('potassium', models.FloatField(verbose_name='Potassium (ppm)')),
                ('organic_matter', models.FloatField(verbose_name='Organic Matter (%)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('fertilizer', models.ForeignKey(to='iwmi.Fertilizer', verbose_name='Fertilizer')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('name', models.CharField(max_length=35, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FuelManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date of use')),
                ('initial_time', models.TimeField(verbose_name='Initial Time')),
                ('final_time', models.TimeField(verbose_name='Final Time')),
                ('amount_used', models.FloatField(verbose_name='Amount Used (Litre)')),
                ('refilled_amount', models.FloatField(verbose_name='Refilled amount (Litre)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('fuel', models.ForeignKey(to='iwmi.Fuel', verbose_name='Fuel')),
            ],
            options={
                'ordering': ['fuel'],
            },
        ),
        migrations.CreateModel(
            name='Furrow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('length', models.FloatField(verbose_name='Length(m)')),
                ('width', models.FloatField(verbose_name='Width(m)')),
                ('numbers', models.IntegerField(verbose_name='Number of furrows')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='GravimetricSoilMoisture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('GroupID', models.CharField(max_length=10, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
            ],
            options={
                'ordering': ['GroupID'],
            },
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Harvest date')),
                ('time', models.FloatField(verbose_name='Time taken')),
                ('amount', models.FloatField(verbose_name='Harvest amount')),
                ('amount_for_home', models.FloatField(verbose_name='Harvest amount for home')),
                ('amount_for_sell', models.FloatField(verbose_name='Harvest amount for sell')),
                ('payement', models.FloatField(null=True, verbose_name='Total payement(Tsh)', blank=True)),
                ('crop', models.ForeignKey(to='iwmi.Crop', verbose_name='Harvested crop')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Harvested farm')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['owner'],
            },
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('NurseryID', models.CharField(max_length=25, verbose_name='Nursery ID', serialize=False, primary_key=True)),
                ('area', models.FloatField(verbose_name='Area(sq.m)')),
                ('date_bed_preparation', models.DateField(verbose_name='Bed Preparation date')),
                ('date_trasplanting', models.DateField(verbose_name='Transplanting date')),
                ('crop', models.ForeignKey(to='iwmi.Crop', verbose_name='Crop')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['NurseryID'],
            },
        ),
        migrations.CreateModel(
            name='NurseryIrrigationEvent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('nursery', models.ForeignKey(to='iwmi.Nursery', verbose_name='Nursery')),
            ],
            options={
                'ordering': ['nursery'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('personID', models.CharField(max_length=45, verbose_name='Person ID', serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=80, verbose_name='First name')),
                ('middlename', models.CharField(null=True, verbose_name='Middle name', max_length=80, blank=True)),
                ('lastname', models.CharField(max_length=80, verbose_name='Last name')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female')])),
                ('role', models.CharField(max_length=40, verbose_name='Role')),
                ('group', models.ForeignKey(to='iwmi.Group', verbose_name='Group')),
            ],
            options={
                'ordering': ['personID'],
            },
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('name', models.CharField(max_length=85, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PesticideManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Application Date')),
                ('form', models.CharField(max_length=20, verbose_name='Form')),
                ('quantity_in_litre', models.FloatField(null=True, verbose_name='Quantity(Litre)', blank=True)),
                ('quantity_in_kg', models.FloatField(null=True, verbose_name='Quantity(Kg)', blank=True)),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('name', models.ForeignKey(to='iwmi.Pesticide', verbose_name='Name')),
                ('personels', models.ManyToManyField(verbose_name='Applied Individual(s)', to='iwmi.People')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('name', models.CharField(max_length=45, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PumpOwnership',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=50, verbose_name='size')),
                ('price', models.FloatField(null=True, verbose_name='Bought price', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Bought date', blank=True)),
                ('group', models.ForeignKey(to='iwmi.Group', verbose_name='Group')),
                ('name', models.ManyToManyField(verbose_name='Name', to='iwmi.Pump')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(max_length=45, verbose_name='region', serialize=False, primary_key=True)),
                ('country', models.ForeignKey(to='iwmi.Country', verbose_name='country')),
            ],
            options={
                'ordering': ['region'],
            },
        ),
        migrations.CreateModel(
            name='RelationManager',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('personA', models.CharField(max_length=25, verbose_name='Person A')),
                ('personB', models.CharField(max_length=25, verbose_name='Person B')),
                ('relation', models.CharField(max_length=20, verbose_name='Relation')),
            ],
        ),
        migrations.CreateModel(
            name='ResidueManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('time_taken', models.FloatField(verbose_name='Time taken')),
                ('burnt', models.BooleanField(verbose_name='Burnt', default=False)),
                ('livestock', models.BooleanField(verbose_name='Used for livestock', default=False)),
                ('purpose', models.TextField(max_length=100, verbose_name='Purpose')),
                ('crop', models.ForeignKey(to='iwmi.Crop', verbose_name='crop')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='SaleHarvestedCrop',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Selling date')),
                ('amount', models.FloatField(verbose_name='Amount sold')),
                ('income', models.FloatField(verbose_name='Total income (Tsh)')),
                ('expenditure', models.FloatField(verbose_name='Expenditure (Tsh)')),
                ('net_income', models.FloatField(verbose_name='Net income (Tsh)')),
                ('crop', models.ForeignKey(to='iwmi.Crop', verbose_name='crop')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('name', models.CharField(max_length=35, verbose_name='Seed', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SeedManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('quantity', models.FloatField(verbose_name='Quantity (kg)')),
                ('price_per_unit', models.FloatField(verbose_name='Price per unit (Tsh)')),
                ('total_cost', models.FloatField(verbose_name='Total cost (Tsh)')),
                ('nursery', models.ForeignKey(to='iwmi.Nursery', verbose_name='Nursery planted on')),
                ('seed', models.ForeignKey(to='iwmi.Seed', verbose_name='Seed')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
                ('repaire_type', models.TextField(max_length=100, verbose_name='Type of repaires')),
                ('price', models.FloatField(verbose_name='Price of spaire parts (Tsh)')),
                ('total_cost', models.FloatField(verbose_name='Total repaire cost (Tsh)')),
                ('group', models.ForeignKey(to='iwmi.Group', verbose_name='Group')),
                ('pump', models.ManyToManyField(verbose_name='Pump', to='iwmi.Pump')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Name', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SoilProperty',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('soilclass', models.ForeignKey(to='iwmi.Soil', verbose_name='Soil class')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Spaire',
            fields=[
                ('name', models.CharField(max_length=45, verbose_name='name', serialize=False, primary_key=True)),
                ('pump', models.ManyToManyField(verbose_name='Pump', to='iwmi.Pump')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SpaireManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('price', models.FloatField(null=True, verbose_name='Bought price (Tsh)', blank=True)),
                ('date', models.DateField(null=True, verbose_name='Bought date', blank=True)),
                ('group', models.ForeignKey(to='iwmi.Group', verbose_name='Group')),
                ('spaire', models.ForeignKey(to='iwmi.Spaire', verbose_name='Spaire')),
            ],
            options={
                'ordering': ['group'],
            },
        ),
        migrations.CreateModel(
            name='TDRMeasurement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('measurement', models.FloatField(verbose_name='Measurement(%)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Technology')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyCalibration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Calibration Date')),
                ('repetition', models.IntegerField(verbose_name='Repetition')),
                ('bucketvolume', models.FloatField(verbose_name='Bucket volume (litre)')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time')),
                ('discharge', models.FloatField(verbose_name='Discharge(m3/s)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('technology', models.ForeignKey(to='iwmi.Technology', verbose_name='Calibrated Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyFailure',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('reason', models.TextField(max_length=100, verbose_name='Reason')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('technology', models.ForeignKey(to='iwmi.Technology', verbose_name='Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyManagement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Installation Date')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('technology', models.ForeignKey(to='iwmi.Technology', verbose_name='Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TissueNutrientAnalysis',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Measurement Date')),
                ('plant_tissue_part', models.CharField(max_length=30, verbose_name='Plant tissue part')),
                ('plantnumber', models.IntegerField(verbose_name='Plant number')),
                ('rownumber', models.IntegerField(verbose_name='Row number')),
                ('freshweight', models.FloatField(verbose_name='Fresh weight(kg)')),
                ('dryweight', models.FloatField(verbose_name='Dry weight(kg)')),
                ('n', models.FloatField(verbose_name='Nitrogen(%)')),
                ('p', models.FloatField(verbose_name='Phosphorus(%)')),
                ('k', models.FloatField(verbose_name='Potassium(%)')),
                ('s', models.FloatField(verbose_name='S(%)')),
                ('mg', models.FloatField(verbose_name='Mg(%)')),
                ('ca', models.FloatField(verbose_name='Ca(%)')),
                ('fe', models.FloatField(verbose_name='Iron(%)')),
                ('zn', models.FloatField(verbose_name='Zinc(%)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('village', models.CharField(max_length=45, verbose_name='village', serialize=False, primary_key=True)),
                ('district', models.ForeignKey(to='iwmi.District', verbose_name='district')),
            ],
            options={
                'ordering': ['village'],
            },
        ),
        migrations.CreateModel(
            name='Weed',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Weeding date')),
                ('weed_activities', models.CharField(max_length=100, verbose_name='What they do')),
                ('time', models.FloatField(verbose_name='Time taken')),
                ('payement', models.FloatField(null=True, verbose_name='Payement(Tsh)', blank=True)),
                ('crop', models.ManyToManyField(verbose_name='Crop(s)', to='iwmi.Crop')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
                ('weeding_personel', models.ManyToManyField(blank=True, verbose_name='Weeding personel(s)', to='iwmi.People')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('depth', models.FloatField(verbose_name='Depth(m)')),
                ('farm', models.ManyToManyField(verbose_name='Farm(s)', to='iwmi.Farm')),
            ],
            options={
                'ordering': ['depth'],
            },
        ),
        migrations.CreateModel(
            name='YieldFarmLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Harvesting Date')),
                ('area', models.FloatField(verbose_name='Area (sq.m)')),
                ('fresh', models.BooleanField(default=False)),
                ('dry', models.BooleanField(default=False)),
                ('marketable_yield', models.FloatField(verbose_name='Marketable yield (Kg)')),
                ('unmarketable_yield', models.FloatField(verbose_name='Unmarketable yield (Kg)')),
                ('biomas', models.FloatField(verbose_name='Biomas (Kg)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='YieldPlantLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('harvest_method', models.CharField(max_length=50, verbose_name='Harvest Method')),
                ('fresh', models.BooleanField(default=False)),
                ('dry', models.BooleanField(default=False)),
                ('nmplant1row1', models.FloatField(verbose_name='NMplant1Row1')),
                ('nmplant2row1', models.FloatField(verbose_name='NMplant2Row1')),
                ('nmplant3row1', models.FloatField(verbose_name='NMplant3Row1')),
                ('nmplant1row2', models.FloatField(verbose_name='NMplant2Row2')),
                ('nmplant2row2', models.FloatField(verbose_name='NMplant2Row2')),
                ('nmplant3row2', models.FloatField(verbose_name='NMplant3Row2')),
                ('nmplant1row3', models.FloatField(verbose_name='NMplant1Row3')),
                ('nmplant2row3', models.FloatField(verbose_name='NMplant2Row3')),
                ('nmplant3row3', models.FloatField(verbose_name='NMplant3Row3')),
                ('numplant1row1', models.FloatField(verbose_name='NUMplant1Row1')),
                ('numplant2row1', models.FloatField(verbose_name='NUMplant2Row1')),
                ('numplant3row1', models.FloatField(verbose_name='NUMplant3Row1')),
                ('numplant1row2', models.FloatField(verbose_name='NUMplant1Row2')),
                ('numplant2row2', models.FloatField(verbose_name='NUMplant2Row2')),
                ('numplant3row2', models.FloatField(verbose_name='NUMplant3Row2')),
                ('numplant1row3', models.FloatField(verbose_name='NUMplant1Row3')),
                ('numplant2row3', models.FloatField(verbose_name='NUMplant2Row3')),
                ('numplant3row3', models.FloatField(verbose_name='NUMplant3Row3')),
                ('wmpl1_row1', models.FloatField(verbose_name='WMPl1 row 1(Kg)')),
                ('wmpl2_row1', models.FloatField(verbose_name='WMPl2 row 1(Kg)')),
                ('wmpl3_row1', models.FloatField(verbose_name='WMPl3 row 1(Kg)')),
                ('wmpl1_row2', models.FloatField(verbose_name='WMPl1 row 2(Kg)')),
                ('wmpl2_row2', models.FloatField(verbose_name='WMPl2 row 2(Kg)')),
                ('wmpl3_row2', models.FloatField(verbose_name='WMPl3 row 2(Kg)')),
                ('wmpl1_row3', models.FloatField(verbose_name='WMPl1 row 3(Kg)')),
                ('wmpl2_row3', models.FloatField(verbose_name='WMPl2 row 3(Kg)')),
                ('wmpl3_row3', models.FloatField(verbose_name='WMPl3 row 3(Kg)')),
                ('wumpl1_row1', models.FloatField(verbose_name='WUMPl1 row 1(Kg)')),
                ('wumpl2_row1', models.FloatField(verbose_name='WUMPl2 row 1(Kg)')),
                ('wumpl3_row1', models.FloatField(verbose_name='WUMPl3 row 1(Kg)')),
                ('wumpl1_row2', models.FloatField(verbose_name='WUMPl1 row 2(Kg)')),
                ('wumpl2_row2', models.FloatField(verbose_name='WUMPl2 row 2(Kg)')),
                ('wumpl3_row2', models.FloatField(verbose_name='WUMPl3 row 2(Kg)')),
                ('wumpl1_row3', models.FloatField(verbose_name='WUMPl1 row 3(Kg)')),
                ('wumpl2_row3', models.FloatField(verbose_name='WUMPl2 row 3(Kg)')),
                ('wumpl3_row3', models.FloatField(verbose_name='WUMPl3 row 3(Kg)')),
                ('diam_WidthP1Row1', models.FloatField(verbose_name='Diam_WidthP1Row1(cm)')),
                ('diam_WidthP2Row1', models.FloatField(verbose_name='Diam_WidthP2Row1(cm)')),
                ('diam_WidthP3Row1', models.FloatField(verbose_name='Diam_WidthP3Row1(cm)')),
                ('diam_WidthP4Row1', models.FloatField(verbose_name='Diam_WidthP4Row1(cm)')),
                ('diam_WidthP5Row1', models.FloatField(verbose_name='Diam_WidthP5Row1(cm)')),
                ('diam_WidthP6Row1', models.FloatField(verbose_name='Diam_WidthP6Row1(cm)')),
                ('diam_WidthP1Row2', models.FloatField(verbose_name='Diam_WidthP1Row2(cm)')),
                ('diam_WidthP2Row2', models.FloatField(verbose_name='Diam_WidthP2Row2(cm)')),
                ('diam_WidthP3Row2', models.FloatField(verbose_name='Diam_WidthP3Row2(cm)')),
                ('diam_WidthP4Row2', models.FloatField(verbose_name='Diam_WidthP4Row2(cm)')),
                ('diam_WidthP5Row2', models.FloatField(verbose_name='Diam_WidthP5Row2(cm)')),
                ('diam_WidthP6Row2', models.FloatField(verbose_name='Diam_WidthP6Row2(cm)')),
                ('diam_WidthP1Row3', models.FloatField(verbose_name='Diam_WidthP1Row3(cm)')),
                ('diam_WidthP2Row3', models.FloatField(verbose_name='Diam_WidthP2Row3(cm)')),
                ('diam_WidthP3Row3', models.FloatField(verbose_name='Diam_WidthP3Row3(cm)')),
                ('diam_WidthP4Row3', models.FloatField(verbose_name='Diam_WidthP4Row3(cm)')),
                ('diam_WidthP5Row3', models.FloatField(verbose_name='Diam_WidthP5Row3(cm)')),
                ('diam_WidthP6Row3', models.FloatField(verbose_name='Diam_WidthP6Row3(cm)')),
                ('lengthP1Row1', models.FloatField(verbose_name='LengthP1Row1(cm)')),
                ('lengthP2Row1', models.FloatField(verbose_name='LengthP2Row1(cm)')),
                ('lengthP3Row1', models.FloatField(verbose_name='LengthP3Row1(cm)')),
                ('lengthP4Row1', models.FloatField(verbose_name='LengthP4Row1(cm)')),
                ('lengthP5Row1', models.FloatField(verbose_name='LengthP5Row1(cm)')),
                ('lengthP6Row1', models.FloatField(verbose_name='LengthP6Row1(cm)')),
                ('lengthP1Row2', models.FloatField(verbose_name='LengthP1Row2(cm)')),
                ('lengthP2Row2', models.FloatField(verbose_name='LengthP2Row2(cm)')),
                ('lengthP3Row2', models.FloatField(verbose_name='LengthP3Row2(cm)')),
                ('lengthP4Row2', models.FloatField(verbose_name='LengthP4Row2(cm)')),
                ('lengthP5Row2', models.FloatField(verbose_name='LengthP5Row2(cm)')),
                ('lengthP6Row2', models.FloatField(verbose_name='LengthP6Row2(cm)')),
                ('lengthP1Row3', models.FloatField(verbose_name='LengthP1Row3(cm)')),
                ('lengthP2Row3', models.FloatField(verbose_name='LengthP2Row3(cm)')),
                ('lengthP3Row3', models.FloatField(verbose_name='LengthP3Row3(cm)')),
                ('lengthP4Row3', models.FloatField(verbose_name='LengthP4Row3(cm)')),
                ('lengthP5Row3', models.FloatField(verbose_name='LengthP5Row3(cm)')),
                ('lengthP6Row3', models.FloatField(verbose_name='LengthP6Row3(cm)')),
                ('Average_length', models.FloatField(verbose_name='Average length(cm)')),
                ('stdev_length', models.FloatField(verbose_name='Stdev Length(cm)')),
                ('residual_biomass_p1_row1', models.FloatField(verbose_name='Residual biomass P1 Row1(Kg)')),
                ('residual_biomass_p2_row1', models.FloatField(verbose_name='Residual biomass P2 Row1(Kg)')),
                ('residual_biomass_p3_row1', models.FloatField(verbose_name='Residual biomass P3 Row1(Kg)')),
                ('residual_biomass_p1_row2', models.FloatField(verbose_name='Residual biomass P1 Row2(Kg)')),
                ('residual_biomass_p2_row2', models.FloatField(verbose_name='Residual biomass P2 Row2(Kg)')),
                ('residual_biomass_p3_row2', models.FloatField(verbose_name='Residual biomass P3 Row2(Kg)')),
                ('residual_biomass_p1_row3', models.FloatField(verbose_name='Residual biomass P1 Row3(Kg)')),
                ('residual_biomass_p2_row3', models.FloatField(verbose_name='Residual biomass P2 Row3(Kg)')),
                ('residual_biomass_p3_row3', models.FloatField(verbose_name='Residual biomass P3 Row3(Kg)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='YieldRowBedLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Harvesting Date')),
                ('harvesting_method', models.CharField(max_length=80, verbose_name='Harvesting method')),
                ('fresh', models.BooleanField(default=False)),
                ('dry', models.BooleanField(default=False)),
                ('sub_plot_area', models.FloatField(verbose_name='Sub plot area(sq.m)')),
                ('nmrow1', models.FloatField(verbose_name='NMROW1')),
                ('nmrow2', models.FloatField(verbose_name='NMROW2')),
                ('nmrow3', models.FloatField(verbose_name='NMROW3')),
                ('numrow1', models.FloatField(verbose_name='NUMROW1')),
                ('numrow2', models.FloatField(verbose_name='NUMROW2')),
                ('numrow3', models.FloatField(verbose_name='NUMROW3')),
                ('wmrow1', models.FloatField(verbose_name='WMROW1(Kg)')),
                ('wmrow2', models.FloatField(verbose_name='WMROW2(Kg)')),
                ('wmrow3', models.FloatField(verbose_name='WMROW3(Kg)')),
                ('wumrow1', models.FloatField(verbose_name='WUMROW1(Kg)')),
                ('wumrow2', models.FloatField(verbose_name='WUMROW2(Kg)')),
                ('wumrow3', models.FloatField(verbose_name='WUMROW3(Kg)')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='service',
            name='spaire',
            field=models.ManyToManyField(verbose_name='Required spaire', to='iwmi.Spaire'),
        ),
        migrations.AddField(
            model_name='people',
            name='village',
            field=models.ForeignKey(to='iwmi.Village', verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(to='iwmi.People', verbose_name='Owner(Farmer)'),
        ),
        migrations.AddField(
            model_name='harvest',
            name='harvest_personel',
            field=models.ForeignKey(null=True, verbose_name='Harvest personel', to='iwmi.People'),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='personels',
            field=models.ManyToManyField(verbose_name='Applied Individual(s)', to='iwmi.People'),
        ),
        migrations.AddField(
            model_name='farmirrigationevent',
            name='technology',
            field=models.ForeignKey(to='iwmi.Technology', verbose_name='Technology'),
        ),
        migrations.AddField(
            model_name='farm',
            name='farmer',
            field=models.ForeignKey(to='iwmi.People', verbose_name='Farmer'),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(to='iwmi.Region', verbose_name='region'),
        ),
        migrations.AddField(
            model_name='croppropertynursery',
            name='nursery',
            field=models.ForeignKey(to='iwmi.Nursery', verbose_name='Nursery'),
        ),
        migrations.AddField(
            model_name='croppropertyfarm',
            name='farm',
            field=models.ForeignKey(to='iwmi.Farm', verbose_name='Farm'),
        ),
        migrations.AddField(
            model_name='croppropertyfarm',
            name='name',
            field=models.ForeignKey(to='iwmi.Crop', verbose_name='Crop'),
        ),
        migrations.AddField(
            model_name='crop',
            name='variety_type',
            field=models.ForeignKey(to='iwmi.CropVariety', verbose_name='Variety type'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='crop',
            field=models.ForeignKey(to='iwmi.Crop', verbose_name='crop'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='farmer',
            field=models.ForeignKey(to='iwmi.People', verbose_name='Farmer'),
        ),
        migrations.AddField(
            model_name='bednursery',
            name='nursery',
            field=models.ForeignKey(to='iwmi.Nursery', verbose_name='NuseryID'),
        ),
        migrations.AddField(
            model_name='bedfarm',
            name='farm',
            field=models.ForeignKey(to='iwmi.Farm', verbose_name='Farm'),
        ),
        migrations.AlterUniqueTogether(
            name='harvest',
            unique_together=set([('farm', 'date')]),
        ),
    ]
