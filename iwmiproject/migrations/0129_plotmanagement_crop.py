# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0128_remove_plotmanagement_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotmanagement',
            name='crop',
            field=models.ManyToManyField(to='iwmiproject.Crop', verbose_name='Crop Name'),
        ),
    ]
