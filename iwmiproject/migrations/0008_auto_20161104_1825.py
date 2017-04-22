# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0007_remove_plotmanagement_water_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotmanagement',
            name='growinglength',
            field=models.IntegerField(verbose_name='Growing length', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='seasonend',
            field=models.DateField(verbose_name='Season end', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='seasonstart',
            field=models.DateField(verbose_name='Season start', null=True, blank=True),
        ),
    ]
