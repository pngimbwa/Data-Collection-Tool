# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0002_people_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='village',
            field=models.ForeignKey(null=True, to='iwmiproject.Village', verbose_name='Village', blank=True),
        ),
    ]
