# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0018_auto_20161106_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourmanagament',
            name='areaID',
            field=models.CharField(blank=True, max_length=35, verbose_name='AreaID', null=True),
        ),
    ]
