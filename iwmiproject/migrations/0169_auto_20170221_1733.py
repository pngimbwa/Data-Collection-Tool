# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0168_saleharvestedcrop_marketprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='income',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total income'),
        ),
    ]
