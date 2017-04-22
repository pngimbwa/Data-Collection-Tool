# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0157_yieldfarmlevel_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldplantlevel',
            name='Crop',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Crop', to='iwmiproject.Crop'),
        ),
    ]
