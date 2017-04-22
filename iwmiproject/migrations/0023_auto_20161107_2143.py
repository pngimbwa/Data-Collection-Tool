# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0022_auto_20161107_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticidemanagement',
            name='price_unit',
            field=models.CharField(blank=True, null=True, max_length=10, verbose_name='Price Unit'),
        ),
    ]
