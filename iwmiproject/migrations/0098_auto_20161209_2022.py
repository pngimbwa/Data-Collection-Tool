# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0097_remove_waterliftingcalibration_plot'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumedCrops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Sell date')),
                ('quantity', models.FloatField(verbose_name='Quantity', blank=True, null=True)),
                ('marketprice', models.FloatField(verbose_name='Market price', blank=True, null=True)),
                ('totalvalue', models.FloatField(verbose_name='Total value', blank=True, null=True)),
                ('currency', models.CharField(verbose_name='Currency', blank=True, max_length=10, null=True)),
                ('enteredpersonel', models.ForeignKey(verbose_name='Entered by', blank=True, to='iwmiproject.SystemUser', null=True)),
                ('farm', models.ForeignKey(verbose_name='Farm', blank=True, to='iwmiproject.Farm', null=True)),
                ('plotID', models.ForeignKey(verbose_name='PlotID', blank=True, to='iwmiproject.Plot', null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='enteredpersonel',
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='plotID',
        ),
        migrations.DeleteModel(
            name='ConsumedCrop',
        ),
    ]
