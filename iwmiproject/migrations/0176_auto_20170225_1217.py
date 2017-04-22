# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0175_auto_20170225_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumpingsource',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='technologymanagement',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Received date'),
        ),
    ]
