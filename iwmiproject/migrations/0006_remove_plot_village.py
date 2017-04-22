# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0005_auto_20161103_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='village',
        ),
    ]
