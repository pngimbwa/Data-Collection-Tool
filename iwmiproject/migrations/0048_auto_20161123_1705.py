# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0047_service_time_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weed',
            name='weed_activities',
            field=models.CharField(max_length=110, verbose_name='What they do'),
        ),
    ]
