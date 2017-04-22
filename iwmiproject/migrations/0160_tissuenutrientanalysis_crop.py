# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0159_yieldrowbedlevel_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='tissuenutrientanalysis',
            name='Crop',
            field=models.ForeignKey(null=True, verbose_name='Crop', blank=True, to='iwmiproject.Crop'),
        ),
    ]
