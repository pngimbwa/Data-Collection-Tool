# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0118_auto_20161230_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='nurseryID_two',
            field=models.CharField(null=True, blank=True, max_length=10, verbose_name='nurseryID for Crop Two'),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='nurseryID_one',
            field=models.CharField(null=True, blank=True, max_length=10, verbose_name='nurseryID for Crop One'),
        ),
    ]
