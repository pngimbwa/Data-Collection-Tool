# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0160_tissuenutrientanalysis_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherwaterusage',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', verbose_name='Entered by', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='remark',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', verbose_name='Entered by', null=True, blank=True),
        ),
    ]
