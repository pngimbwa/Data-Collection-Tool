# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0029_auto_20161112_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumedcrop',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='crop',
        ),
        migrations.RemoveField(
            model_name='consumedcrop',
            name='farm',
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='currency',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='marketprice',
            field=models.FloatField(null=True, blank=True, verbose_name='Market price'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='plotID',
            field=models.ForeignKey(null=True, to='iwmiproject.Plot', blank=True, verbose_name='PlotID'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='quantity',
            field=models.FloatField(null=True, blank=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='totalvalue',
            field=models.FloatField(null=True, blank=True, verbose_name='Total value'),
        ),
    ]
