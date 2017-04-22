# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0173_auto_20170224_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='fieldtype',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='Fieldtype'),
        ),
    ]
