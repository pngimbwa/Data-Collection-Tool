# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0131_plot_landownership'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotcrop',
            name='crop1_planting_method',
            field=models.CharField(max_length=100, blank=True, verbose_name='Planting Method', null=True),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop2_planting_method',
            field=models.CharField(max_length=100, blank=True, verbose_name='Planting Method', null=True),
        ),
    ]
