# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0111_plotcrop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='crop',
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='crop',
            field=models.ManyToManyField(verbose_name='Crop Name(s)', to='iwmiproject.Crop'),
        ),
    ]
