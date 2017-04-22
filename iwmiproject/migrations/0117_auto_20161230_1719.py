# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0116_auto_20161230_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='total_seed_quantity',
            field=models.IntegerField(verbose_name='Total seed quantity', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='nurseryID_one',
            field=models.ForeignKey(verbose_name='nurseryID for Crop One', blank=True, to='iwmiproject.Nursery', null=True),
        ),
    ]
