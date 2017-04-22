# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0007_auto_20161013_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizermanagement',
            name='form',
            field=models.CharField(verbose_name='Form', max_length=20),
        ),
        migrations.AlterField(
            model_name='fertilizermanagement',
            name='price',
            field=models.FloatField(verbose_name='Price(Tsh)'),
        ),
        migrations.AlterField(
            model_name='well',
            name='diameter',
            field=models.FloatField(verbose_name='Diameter(m)'),
        ),
    ]
