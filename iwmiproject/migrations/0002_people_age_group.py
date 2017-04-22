# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='age_group',
            field=models.CharField(max_length=10, null=True, verbose_name='Age group', blank=True),
        ),
    ]
