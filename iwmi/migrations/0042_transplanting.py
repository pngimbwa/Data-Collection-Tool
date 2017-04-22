# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0041_remove_yieldplantlevel_farm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transplanting',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='transplanting date')),
                ('plantsnumber', models.IntegerField(verbose_name='Total number of plants transplanted')),
                ('plant_spacing_btn_row', models.FloatField(verbose_name='Plant spacing between row(cm)')),
                ('plant_spacing_btn_plants_within_rows', models.FloatField(verbose_name='Plant spacing between plants within rows(cm)')),
                ('plantsnumber_per_row', models.IntegerField(verbose_name='Plant number per row')),
                ('nurseryID', models.ForeignKey(null=True, blank=True, to='iwmi.Nursery', verbose_name='nurseryID')),
                ('plotID', models.ForeignKey(null=True, blank=True, to='iwmi.Plot', verbose_name='PlotID')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
    ]
