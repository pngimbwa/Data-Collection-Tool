# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0152_auto_20170131_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumedcrops',
            name='how_consumed',
            field=models.CharField(null=True, max_length=20, verbose_name='How consumed', blank=True),
        ),
        migrations.AlterField(
            model_name='consumedcrops',
            name='where_consumed',
            field=models.CharField(null=True, max_length=20, verbose_name='Where consumed', blank=True),
        ),
    ]
