# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0059_auto_20161125_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='plantsnumber',
            field=models.IntegerField(verbose_name='Total number of plants transplanted', null=True, blank=True),
        ),
    ]
