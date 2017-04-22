# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0074_otherwaterusage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherwaterusage',
            name='end_time',
            field=models.TimeField(verbose_name='End time', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='otherwaterusage',
            name='start_time',
            field=models.TimeField(verbose_name='Start time', blank=True, null=True),
        ),
    ]
