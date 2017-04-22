# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0124_remove_plotmanagement_growinglength'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotirrigationevent',
            name='service_provider',
            field=models.CharField(verbose_name='Service Provider', blank=True, max_length=4, null=True),
        ),
    ]
