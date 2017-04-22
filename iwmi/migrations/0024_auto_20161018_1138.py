# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0023_auto_20161018_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weed',
            name='payement',
        ),
        migrations.RemoveField(
            model_name='weed',
            name='weeding_personel',
        ),
        migrations.RemoveField(
            model_name='weed',
            name='crop',
        ),
        migrations.AddField(
            model_name='weed',
            name='crop',
            field=models.ForeignKey(verbose_name='Crop(s)', default='o', to='iwmi.Crop'),
        ),
    ]
