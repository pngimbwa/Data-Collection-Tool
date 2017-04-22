# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0063_auto_20161126_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weed',
            name='time',
        ),
    ]
