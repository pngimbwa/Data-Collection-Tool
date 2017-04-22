# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0048_auto_20161123_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weed',
            name='weed_activities',
            field=models.CharField(max_length=80, verbose_name='What they do'),
        ),
    ]
