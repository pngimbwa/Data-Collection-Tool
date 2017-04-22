# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0038_auto_20161101_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesticidemanagement',
            name='farm',
        ),
    ]
