# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0165_delete_pointofinterest'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='quantity_harvested',
            field=models.FloatField(blank=True, verbose_name='Harvested Amount (kg)', null=True),
        ),
    ]
