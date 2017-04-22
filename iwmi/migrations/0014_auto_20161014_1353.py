# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0013_auto_20161014_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='crop',
            field=models.ForeignKey(to='iwmi.Crop', verbose_name='Crop(s)'),
        ),
    ]
