# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0115_auto_20161228_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantingmethod',
            old_name='nurseryID',
            new_name='nurseryID_one',
        ),
    ]
