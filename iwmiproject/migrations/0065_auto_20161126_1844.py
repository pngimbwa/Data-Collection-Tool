# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0064_remove_weed_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='plotID',
            field=models.ForeignKey(null=True, verbose_name='Farm', blank=True, to='iwmiproject.Plot'),
        ),
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='farm',
            field=models.ForeignKey(null=True, verbose_name='Farm', blank=True, to='iwmiproject.Farm'),
        ),
    ]
