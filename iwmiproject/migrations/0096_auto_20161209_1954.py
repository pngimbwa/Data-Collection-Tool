# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0095_auto_20161209_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='consumedcrop',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='harvest',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='landclearance',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='landpreparation',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
        migrations.AddField(
            model_name='waterliftingcalibration',
            name='farm',
            field=models.ForeignKey(null=True, to='iwmiproject.Farm', verbose_name='Farm', blank=True),
        ),
    ]
