# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0008_auto_20161104_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bedplot',
            name='planting_density',
        ),
        migrations.AlterField(
            model_name='plotmanagement',
            name='growinglength',
            field=models.IntegerField(verbose_name='Growing length(days)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plotmanagement',
            name='seasonend',
            field=models.DateField(verbose_name='Season ended', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plotmanagement',
            name='seasonstart',
            field=models.DateField(verbose_name='Season started', null=True, blank=True),
        ),
    ]
