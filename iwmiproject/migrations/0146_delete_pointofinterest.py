# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0145_auto_20170128_1042'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PointOfInterest',
        ),
    ]
