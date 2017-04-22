# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0142_auto_20170127_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_management_practice',
            field=models.CharField(blank=True, verbose_name='Crop one Management practice', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_management_practice',
            field=models.CharField(blank=True, verbose_name='Crop two management practice', max_length=15, null=True),
        ),
    ]
