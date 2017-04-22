# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0178_auto_20170227_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yieldplantlevel',
            name='fresh_dry',
            field=models.CharField(blank=True, null=True, max_length=15, verbose_name='Fresh/Dry'),
        ),
    ]
