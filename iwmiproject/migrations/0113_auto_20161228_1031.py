# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0112_auto_20161228_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotmanagement',
            name='crop',
            field=models.ManyToManyField(verbose_name='Crop Name', to='iwmiproject.Crop'),
        ),
    ]
