# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0021_auto_20161017_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yieldfarmlevel',
            name='dry',
        ),
        migrations.RemoveField(
            model_name='yieldfarmlevel',
            name='fresh',
        ),
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='fresh_dry',
            field=models.CharField(null=True, verbose_name='Fresh/Dry', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='yieldplantlevel',
            name='fresh_dry',
            field=models.CharField(verbose_name='Fresh/Dry', max_length=10),
        ),
    ]
