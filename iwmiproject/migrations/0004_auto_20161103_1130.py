# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0003_auto_20161102_2327'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pumpingsource',
            unique_together=set([]),
        ),
    ]
