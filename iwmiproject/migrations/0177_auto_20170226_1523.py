# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0176_auto_20170225_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remark',
            name='date',
        ),
        migrations.AddField(
            model_name='remark',
            name='end_date',
            field=models.DateField(null=True, blank=True, verbose_name='Stress end Date'),
        ),
        migrations.AddField(
            model_name='remark',
            name='start_date',
            field=models.DateField(null=True, blank=True, verbose_name='Stress start date'),
        ),
    ]
