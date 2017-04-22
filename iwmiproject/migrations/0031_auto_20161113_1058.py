# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0030_auto_20161113_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yieldfarmlevel',
            name='area',
        ),
        migrations.RemoveField(
            model_name='yieldfarmlevel',
            name='farm',
        ),
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='plotID',
            field=models.ForeignKey(blank=True, verbose_name='Plot ID', to='iwmiproject.Plot', null=True),
        ),
    ]
