# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0069_yieldplantlevel_row_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='row_number',
            field=models.IntegerField(blank=True, verbose_name='Row number', null=True),
        ),
    ]
