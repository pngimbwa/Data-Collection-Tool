# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0007_auto_20161202_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(default='8686FD', unique=True, blank=True, max_length=100),
        ),
    ]
