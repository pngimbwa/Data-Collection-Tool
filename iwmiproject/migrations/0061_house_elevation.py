# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0060_plantingmethod_plantsnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='elevation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
