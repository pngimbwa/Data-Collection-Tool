# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0098_auto_20161209_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterliftingCalibrations',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('event', models.IntegerField(verbose_name='Event number', null=True, blank=True)),
                ('waterlevel', models.FloatField(verbose_name='Water level(m)', null=True, blank=True)),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time(mins)')),
                ('bucket_volume', models.FloatField(verbose_name='Bucket volume', null=True, blank=True)),
                ('discharge', models.FloatField(verbose_name='Discharge(L/s)', null=True, blank=True)),
                ('enteredpersonel', models.ForeignKey(to='iwmiproject.SystemUser', null=True, blank=True, verbose_name='Entered by')),
                ('farm', models.ForeignKey(to='iwmiproject.Farm', null=True, blank=True, verbose_name='Farm')),
                ('technology', models.ForeignKey(to='iwmiproject.Technology', verbose_name='Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='waterliftingcalibration',
            name='enteredpersonel',
        ),
        migrations.RemoveField(
            model_name='waterliftingcalibration',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='waterliftingcalibration',
            name='technology',
        ),
        migrations.DeleteModel(
            name='WaterliftingCalibration',
        ),
    ]
