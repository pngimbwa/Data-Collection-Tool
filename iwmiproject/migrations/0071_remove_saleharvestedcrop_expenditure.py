# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0070_yieldrowbedlevel_row_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleharvestedcrop',
            name='expenditure',
        ),
    ]
