# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0033_auto_20161120_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='red_WFD_before_irrigation',
            field=models.CharField(max_length=4, null=True, verbose_name='Red WFD before irrigation', blank=True),
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='yellow_WFD_before_irrigation',
            field=models.CharField(max_length=4, null=True, verbose_name='Yellow WFD before irrigation', blank=True),
        ),
    ]
