# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0137_auto_20170125_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='planting_method',
            field=models.CharField(null=True, verbose_name='Planting Method', blank=True, max_length=100),
        ),
    ]
