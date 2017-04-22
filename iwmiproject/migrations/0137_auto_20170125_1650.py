# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0136_auto_20170125_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourmanagament',
            name='areaID',
            field=models.CharField(null=True, blank=True, max_length=60, verbose_name='AreaID'),
        ),
    ]
