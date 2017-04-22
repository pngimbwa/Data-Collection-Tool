# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0032_auto_20161101_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('planting_method', models.CharField(max_length=100, verbose_name='Planting Method')),
                ('seeding_date', models.DateField(blank=True, verbose_name='Seeding Date', null=True)),
                ('planting_date', models.DateField(blank=True, verbose_name='Planting date', null=True)),
                ('seeding_rate', models.FloatField(blank=True, verbose_name='seeding rate', null=True)),
                ('seed_spacing_within_a_row', models.FloatField(blank=True, verbose_name='seed spacing within a row(cm)', null=True)),
                ('seed_spacing_btn_a_row', models.FloatField(blank=True, verbose_name='seed spacing btn a row(cm)', null=True)),
                ('plotID', models.ForeignKey(to='iwmi.Plot', verbose_name='PlotID', blank=True, null=True)),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='elevation',
            field=models.FloatField(blank=True, verbose_name='elevation', null=True),
        ),
        migrations.AlterField(
            model_name='pumpingsource',
            name='latitude',
            field=models.FloatField(verbose_name="Source's latitude"),
        ),
        migrations.AlterField(
            model_name='pumpingsource',
            name='longitude',
            field=models.FloatField(verbose_name="Source's longitude"),
        ),
    ]
