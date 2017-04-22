# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0087_auto_20161207_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherwaterusage',
            name='plot',
        ),
    ]
