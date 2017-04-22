# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0005_auto_20161130_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(default='DA1783', unique=True, blank=True, max_length=100),
        ),
    ]
