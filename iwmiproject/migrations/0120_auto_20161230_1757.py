# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0119_auto_20161230_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingmethod',
            name='nurseryID_one',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='nurseryID_two',
        ),
    ]
