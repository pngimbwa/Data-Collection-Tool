# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0004_auto_20161103_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationmanager',
            name='family_member',
            field=models.ManyToManyField(verbose_name='Household members', to='iwmiproject.People'),
        ),
        migrations.AlterField(
            model_name='relationmanager',
            name='relation',
            field=models.CharField(max_length=20, verbose_name='Relation', default='Family'),
        ),
    ]
