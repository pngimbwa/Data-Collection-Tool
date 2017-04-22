# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0031_auto_20161101_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmtotalplotnumber',
            name='farm',
        ),
        migrations.AlterField(
            model_name='plot',
            name='farm',
            field=models.ForeignKey(to='iwmi.Farm', verbose_name='FarmID'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='plotID',
            field=models.CharField(max_length=50, verbose_name='PlotID'),
        ),
        migrations.AlterUniqueTogether(
            name='plot',
            unique_together=set([('farm', 'plotID')]),
        ),
        migrations.DeleteModel(
            name='FarmTotalPlotNumber',
        ),
    ]
