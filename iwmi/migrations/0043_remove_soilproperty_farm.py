# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0042_transplanting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soilproperty',
            name='farm',
        ),
    ]
