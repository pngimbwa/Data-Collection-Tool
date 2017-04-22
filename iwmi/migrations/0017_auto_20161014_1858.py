# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0016_auto_20161014_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursery',
            name='seed',
            field=models.ForeignKey(to='iwmi.Seed', verbose_name='seed'),
        ),
    ]
