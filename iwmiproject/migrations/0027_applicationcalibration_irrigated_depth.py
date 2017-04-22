# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0026_applicationcalibration'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='irrigated_depth',
            field=models.FloatField(verbose_name='Irrigated depth(cm)', blank=True, null=True),
        ),
    ]
