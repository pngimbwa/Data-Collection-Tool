# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0037_auto_20161122_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourmanagament',
            name='time_taken',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken'),
        ),
    ]
