# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0010_auto_20161105_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='water_management_method',
        ),
    ]
