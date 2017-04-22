# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0106_nurseryirrigationevent_irrigation_depth'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plot',
            unique_together=set([('plotID', 'farm')]),
        ),
    ]
