# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0101_remove_nursery_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursery',
            name='seed',
            field=models.ForeignKey(verbose_name='seed', to='iwmiproject.Seed', null=True, blank=True),
        ),
    ]
