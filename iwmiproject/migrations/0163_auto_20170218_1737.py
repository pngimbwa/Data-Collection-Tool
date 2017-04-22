# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0162_auto_20170218_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel2',
            name='house',
        ),
        migrations.DeleteModel(
            name='Hostel2',
        ),
        migrations.DeleteModel(
            name='House2',
        ),
    ]
