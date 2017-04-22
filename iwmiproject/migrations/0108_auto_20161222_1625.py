# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0107_auto_20161220_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotmanagement',
            name='management_practice',
            field=models.CharField(max_length=10, blank=True, verbose_name='Management practice', null=True),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='mulching_quantity',
            field=models.FloatField(blank=True, verbose_name='Mulching quantity', null=True),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='mulching_type',
            field=models.CharField(max_length=45, blank=True, verbose_name='Mulching type', null=True),
        ),
    ]
