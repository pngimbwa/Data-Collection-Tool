# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0177_auto_20170226_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yieldplantlevel',
            name='fresh_dry',
            field=models.CharField(null=True, verbose_name='Fresh/Dry', max_length=10, blank=True),
        ),
    ]
