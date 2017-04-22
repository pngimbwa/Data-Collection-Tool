# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0026_auto_20161023_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='variety_type',
        ),
        migrations.DeleteModel(
            name='CropVariety',
        ),
    ]
