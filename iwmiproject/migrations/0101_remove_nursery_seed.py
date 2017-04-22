# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0100_auto_20161212_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='seed',
        ),
    ]
