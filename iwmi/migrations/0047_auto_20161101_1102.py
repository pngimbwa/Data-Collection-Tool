# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0046_auto_20161101_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandClearance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('landclearanceoption', models.CharField(verbose_name='Land clearance option', max_length=50)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmi.Plot')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.CreateModel(
            name='LandPreparation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Land preparation date')),
                ('landpreparationtool', models.CharField(verbose_name='Land preparation tool', max_length=50)),
                ('plotID', models.ForeignKey(null=True, blank=True, verbose_name='PlotID', to='iwmi.Plot')),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='farmer',
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='farm',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Farm', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='price_unit',
            field=models.CharField(default='Tsh', verbose_name='Currency', max_length=10),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='wage',
            field=models.FloatField(verbose_name='Daily wage'),
        ),
    ]
