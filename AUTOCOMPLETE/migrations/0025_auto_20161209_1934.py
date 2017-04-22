# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0024_auto_20161209_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(default='347208', blank=True, unique=True, max_length=100),
        ),
    ]
