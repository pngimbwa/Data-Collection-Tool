# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0151_auto_20170131_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumedcrops',
            name='how_consumed',
            field=models.CharField(verbose_name='How consumed', null=True, max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='consumedcrops',
            name='where_consumed',
            field=models.CharField(verbose_name='Where consumed', null=True, max_length=10, blank=True),
        ),
    ]
