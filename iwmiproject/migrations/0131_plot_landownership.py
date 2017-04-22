# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0130_auto_20170123_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='landownership',
            field=models.CharField(verbose_name='Plot Ownership', blank=True, max_length=10, null=True),
        ),
    ]
