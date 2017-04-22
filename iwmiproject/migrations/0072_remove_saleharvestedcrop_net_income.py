# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0071_remove_saleharvestedcrop_expenditure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleharvestedcrop',
            name='net_income',
        ),
    ]
