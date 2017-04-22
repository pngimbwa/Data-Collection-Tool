# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0029_auto_20161026_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizermanagement',
            name='s',
            field=models.FloatField(null=True, verbose_name='S(g/kg)', blank=True),
        ),
    ]
