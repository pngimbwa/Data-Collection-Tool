# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0110_fertilizermanagement_compost_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotCrop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('crop1', models.CharField(null=True, verbose_name='Crop One', max_length=30, blank=True)),
                ('crop1_variety', models.CharField(null=True, verbose_name='Crop_one variety', max_length=70, blank=True)),
                ('crop1_varietytype', models.CharField(null=True, verbose_name='Crop_one variety Type', max_length=20, blank=True)),
                ('crop2', models.CharField(null=True, verbose_name='Crop Two', max_length=30, blank=True)),
                ('crop2_variety', models.CharField(null=True, verbose_name='Crop_two variety', max_length=70, blank=True)),
                ('crop2_varietytype', models.CharField(null=True, verbose_name='Crop_two variety Type', max_length=20, blank=True)),
                ('farm', models.ForeignKey(verbose_name='FarmID', to='iwmiproject.Farm', blank=True, null=True)),
                ('plotID', models.ForeignKey(verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['farm'],
            },
        ),
    ]
