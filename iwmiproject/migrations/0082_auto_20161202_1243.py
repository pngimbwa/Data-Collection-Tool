# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0081_auto_20161201_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='tanknumber',
            field=models.IntegerField(verbose_name='Number of Tanks', null=True, blank=True),
        ),
    ]
