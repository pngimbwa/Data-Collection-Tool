# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0017_auto_20161014_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='form',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='quantity_in_litre',
        ),
    ]
