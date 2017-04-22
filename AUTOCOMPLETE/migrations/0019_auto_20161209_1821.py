# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0018_auto_20161207_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(unique=True, max_length=100, blank=True, default='72EA04'),
        ),
    ]
