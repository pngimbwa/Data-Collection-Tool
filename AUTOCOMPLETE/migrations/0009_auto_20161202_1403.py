# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0008_auto_20161202_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(null=True, blank=True, upload_to='cars'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(unique=True, default='682DF5', max_length=100, blank=True),
        ),
    ]
