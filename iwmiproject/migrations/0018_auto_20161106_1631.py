# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0017_auto_20161106_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seedmanagement',
            name='seed_spacing_btn_bed',
        ),
        migrations.RemoveField(
            model_name='seedmanagement',
            name='seed_spacing_within_a_bed',
        ),
        migrations.AddField(
            model_name='bednursery',
            name='seed_spacing_btn_bed',
            field=models.FloatField(blank=True, null=True, verbose_name='seed spacing btn bed/row(m)'),
        ),
        migrations.AddField(
            model_name='bednursery',
            name='seed_spacing_within_a_bed',
            field=models.FloatField(blank=True, null=True, verbose_name='seed spacing within a bed/row(m)'),
        ),
    ]
