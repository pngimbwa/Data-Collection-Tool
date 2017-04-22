# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0104_nursery_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizermanagement',
            name='nurseryID',
            field=models.ForeignKey(null=True, verbose_name='nurseryID', to='iwmiproject.Nursery', blank=True),
        ),
    ]
