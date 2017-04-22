# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0073_auto_20161128_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherWaterUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('bucketnumber', models.FloatField(verbose_name='Bucket number', blank=True, null=True)),
                ('bucketvolume', models.FloatField(verbose_name='Bucket volume (L)', blank=True, null=True)),
                ('usagepurpose', models.CharField(verbose_name='Usage', blank=True, null=True, max_length=45)),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('total_time', models.FloatField(verbose_name='Total time', blank=True, null=True)),
                ('totalvolume', models.FloatField(verbose_name='Total volume (L)', blank=True, null=True)),
                ('lifting_technology_yes_no', models.CharField(verbose_name='Lifting technology (Yes/No)', blank=True, null=True, max_length=4)),
                ('farm', models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm')),
                ('plot', models.ForeignKey(verbose_name='Plot', to='iwmiproject.Plot')),
                ('technology', models.ForeignKey(verbose_name='Technology', to='iwmiproject.Technology')),
            ],
        ),
    ]
