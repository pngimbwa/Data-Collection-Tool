# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0156_auto_20170203_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='Crop',
            field=models.ForeignKey(null=True, verbose_name='Crop', to='iwmiproject.Crop', blank=True),
        ),
    ]
