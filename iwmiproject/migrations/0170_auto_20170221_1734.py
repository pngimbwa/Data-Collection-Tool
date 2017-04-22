# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0169_auto_20170221_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleharvestedcrop',
            name='amount',
            field=models.IntegerField(blank=True, verbose_name='Amount sold', null=True),
        ),
    ]
