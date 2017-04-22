# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0028_auto_20161112_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gravimetricsoilmoisture',
            name='time',
        ),
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='time_taken',
            field=models.FloatField(blank=True, verbose_name='Time taken(mins)', null=True),
        ),
    ]
