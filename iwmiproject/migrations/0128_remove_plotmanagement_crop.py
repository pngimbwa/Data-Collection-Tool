# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0127_auto_20170113_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='crop',
        ),
    ]
