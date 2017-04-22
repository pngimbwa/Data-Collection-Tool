# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0153_auto_20170131_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotcrop',
            name='cropping_system',
            field=models.CharField(max_length=20, verbose_name='Cropping System', blank=True, null=True),
        ),
    ]
