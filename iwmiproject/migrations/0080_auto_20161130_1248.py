# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0079_remove_plotirrigationevent_bucketdiameter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingmethod',
            name='plantsnumber',
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='bucketdiameter',
            field=models.FloatField(null=True, blank=True, verbose_name='Bucket/Tank diameter(cm)'),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='bucketnumbers',
            field=models.FloatField(null=True, blank=True, verbose_name='Number of buckets/Tanks'),
        ),
        migrations.AlterField(
            model_name='applicationcalibration',
            name='bucketvolume',
            field=models.FloatField(null=True, blank=True, verbose_name='Bucket/Tank volume(L)'),
        ),
    ]
