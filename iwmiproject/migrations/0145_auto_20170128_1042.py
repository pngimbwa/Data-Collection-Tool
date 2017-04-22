# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0144_pointofinterest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pointofinterest',
            options={'ordering': ['name']},
        ),
    ]
