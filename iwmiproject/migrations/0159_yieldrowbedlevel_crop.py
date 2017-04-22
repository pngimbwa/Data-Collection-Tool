# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0158_yieldplantlevel_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='Crop',
            field=models.ForeignKey(to='iwmiproject.Crop', verbose_name='Crop', null=True, blank=True),
        ),
    ]
