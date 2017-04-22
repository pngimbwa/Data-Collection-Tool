# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0048_systemuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationmanager',
            options={'ordering': ['farmer']},
        ),
        migrations.RemoveField(
            model_name='farm',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='relationmanager',
            name='personA',
        ),
        migrations.RemoveField(
            model_name='relationmanager',
            name='personB',
        ),
        migrations.AddField(
            model_name='farm',
            name='total_irrigated_plots',
            field=models.IntegerField(verbose_name='Number of irrigated plots'),
        ),
        migrations.AddField(
            model_name='farm',
            name='total_irrigated_plots_land_area',
            field=models.FloatField(verbose_name='Total irrigated plots land area (sq.m)'),
        ),
        migrations.AddField(
            model_name='plot',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='plot',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='relationmanager',
            name='family_member',
            field=models.ManyToManyField(verbose_name='Household family members', to='iwmi.People'),
        ),
        migrations.AddField(
            model_name='relationmanager',
            name='farmer',
            field=models.CharField(verbose_name='farmer', max_length=25),
        ),
        migrations.AlterField(
            model_name='relationmanager',
            name='relation',
            field=models.CharField(default='Household member', verbose_name='Relation', max_length=20),
        ),
    ]
