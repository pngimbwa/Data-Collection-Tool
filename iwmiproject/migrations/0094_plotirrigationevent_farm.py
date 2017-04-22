# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0093_auto_20161209_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotirrigationevent',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farm', to='iwmiproject.Farm'),
        ),
    ]
