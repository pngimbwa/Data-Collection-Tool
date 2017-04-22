# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0089_auto_20161209_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='farm',
            field=models.ForeignKey(null=True, verbose_name='Farm', to='iwmiproject.Farm', blank=True),
        ),
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='farm',
            field=models.ForeignKey(null=True, verbose_name='Farm', to='iwmiproject.Farm', blank=True),
        ),
    ]
