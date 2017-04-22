# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0090_auto_20161209_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='farm',
            field=models.ForeignKey(null=True, verbose_name='Farm', blank=True, to='iwmiproject.Farm'),
        ),
    ]
