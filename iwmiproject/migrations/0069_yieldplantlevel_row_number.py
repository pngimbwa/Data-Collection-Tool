# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0068_cropmonitoringplantheight_lai'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldplantlevel',
            name='row_number',
            field=models.IntegerField(verbose_name='Row number', blank=True, null=True),
        ),
    ]
