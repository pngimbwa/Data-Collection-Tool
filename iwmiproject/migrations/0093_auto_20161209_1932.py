# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0092_auto_20161209_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, verbose_name='Farm', null=True),
        ),
        migrations.AddField(
            model_name='soilmoisturemeasurementmanagement',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, verbose_name='Farm', null=True),
        ),
        migrations.AddField(
            model_name='soilmoistureprofiler',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, verbose_name='Farm', null=True),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, verbose_name='Farm', null=True),
        ),
        migrations.AddField(
            model_name='tissuenutrientanalysis',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', blank=True, verbose_name='Farm', null=True),
        ),
    ]
