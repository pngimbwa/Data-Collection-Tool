# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0041_auto_20161123_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticidemanagement',
            name='water_volume',
            field=models.FloatField(verbose_name='Water volume(L)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bednursery',
            name='seed_spacing_btn_bed',
            field=models.FloatField(verbose_name='seed spacing btn bed/row(cm)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bednursery',
            name='seed_spacing_within_a_bed',
            field=models.FloatField(verbose_name='seed spacing within a bed/row(cm)', null=True, blank=True),
        ),
    ]
