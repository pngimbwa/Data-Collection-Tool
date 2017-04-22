# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0002_cropmonitoringplantheight'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='phone',
            field=models.CharField(default=datetime.datetime(2016, 10, 12, 12, 43, 39, 644705, tzinfo=utc), max_length=50, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]
