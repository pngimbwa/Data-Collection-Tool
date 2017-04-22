# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0102_nursery_seed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='seed',
        ),
        migrations.AlterField(
            model_name='cropvarieties',
            name='varietytype',
            field=models.CharField(max_length=20, verbose_name='Variety Type'),
        ),
    ]
