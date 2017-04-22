# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0037_auto_20161101_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='s',
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='sulphur',
            field=models.FloatField(blank=True, verbose_name='Sulphur(g/kg)', null=True),
        ),
    ]
