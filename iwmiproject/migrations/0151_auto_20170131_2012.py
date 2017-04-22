# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0150_auto_20170131_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterliftingcalibrations',
            name='age_group',
            field=models.CharField(null=True, blank=True, max_length=15, verbose_name='Age group'),
        ),
        migrations.AddField(
            model_name='waterliftingcalibrations',
            name='gender',
            field=models.CharField(null=True, blank=True, max_length=10, verbose_name='Gender'),
        ),
    ]
