# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0024_auto_20161018_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weed',
            name='crop',
            field=models.ForeignKey(to='iwmi.Crop', verbose_name='Crop(s)'),
        ),
    ]
