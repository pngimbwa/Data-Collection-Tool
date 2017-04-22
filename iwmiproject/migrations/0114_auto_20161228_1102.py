# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0113_auto_20161228_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotmanagement',
            name='cropping_system',
            field=models.CharField(verbose_name='Cropping System', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='plotmanagement',
            name='crop',
            field=models.ManyToManyField(to='iwmiproject.Crop', blank=True, null=True, verbose_name='Crop Name'),
        ),
    ]
