# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0065_auto_20161126_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleharvestedcrop',
            name='farm',
        ),
    ]
