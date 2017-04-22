# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0004_auto_20161012_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(max_length=10, verbose_name='Gender'),
        ),
    ]
