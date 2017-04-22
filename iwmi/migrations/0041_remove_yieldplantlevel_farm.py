# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0040_auto_20161101_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yieldplantlevel',
            name='farm',
        ),
    ]
