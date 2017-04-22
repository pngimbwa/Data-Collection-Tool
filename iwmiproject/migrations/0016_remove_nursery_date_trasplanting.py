# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0015_auto_20161106_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='date_trasplanting',
        ),
    ]
