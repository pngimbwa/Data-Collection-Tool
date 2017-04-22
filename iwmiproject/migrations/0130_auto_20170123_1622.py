# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0129_plotmanagement_crop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotmanagement',
            name='date',
            field=models.DateField(null=True, verbose_name='Date', blank=True),
        ),
    ]
