# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0044_auto_20161101_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soilmoisturemeasurementmanagement',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='soilmoistureprofiler',
            name='farm',
        ),
    ]
