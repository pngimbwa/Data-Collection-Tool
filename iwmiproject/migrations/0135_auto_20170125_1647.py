# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0134_auto_20170125_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourmanagament',
            name='labour',
            field=models.CharField(verbose_name='Labour', max_length=45),
        ),
    ]
