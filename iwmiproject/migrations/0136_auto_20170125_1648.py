# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0135_auto_20170125_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourmanagament',
            name='areadescription',
            field=models.CharField(blank=True, null=True, max_length=40, verbose_name='Area description'),
        ),
    ]
