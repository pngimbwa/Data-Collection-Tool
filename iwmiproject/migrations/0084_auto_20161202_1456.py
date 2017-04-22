# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0083_auto_20161202_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemuser',
            options={'ordering': ['user'], 'permissions': (('image', 'Can add image'),)},
        ),
    ]
