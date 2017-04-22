# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0046_remove_service_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='time_taken',
            field=models.FloatField(verbose_name='Time taken(hr)', null=True, blank=True),
        ),
    ]
