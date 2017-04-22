# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0005_auto_20161012_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], verbose_name='Gender', max_length=10),
        ),
    ]
