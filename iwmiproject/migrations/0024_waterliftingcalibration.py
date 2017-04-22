# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0023_auto_20161107_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterliftingCalibration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('event', models.IntegerField(null=True, blank=True, verbose_name='Event number')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time(mins)')),
                ('bucket_volume', models.FloatField(null=True, blank=True, verbose_name='Bucket volume')),
                ('discharge', models.FloatField(null=True, blank=True, verbose_name='Discharge')),
                ('enteredpersonel', models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True)),
                ('plot', models.ForeignKey(to='iwmiproject.Plot', verbose_name='Farm')),
                ('technology', models.ForeignKey(to='iwmiproject.Technology', verbose_name='Technology')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
