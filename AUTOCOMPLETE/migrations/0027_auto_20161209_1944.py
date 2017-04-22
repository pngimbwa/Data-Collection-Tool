# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0026_auto_20161209_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(default='9E4244', max_length=100, blank=True, unique=True),
        ),
    ]
