# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0122_auto_20161230_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='seasonend',
        ),
    ]
