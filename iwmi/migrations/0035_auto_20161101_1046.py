# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0034_auto_20161101_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotCultivation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Cultivation date')),
                ('cultivation_method', models.CharField(max_length=80, verbose_name='Method of Cultivation')),
                ('plotID', models.ForeignKey(to='iwmi.Plot', verbose_name='PlotID')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='farmcultivation',
            name='farm',
        ),
        migrations.DeleteModel(
            name='FarmCultivation',
        ),
    ]
