# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0109_auto_20161223_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizermanagement',
            name='compost_kind',
            field=models.CharField(max_length=45, verbose_name='Compost kind', default='None'),
        ),
    ]
