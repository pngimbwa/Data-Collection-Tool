# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0170_auto_20170221_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='bednursery',
            name='enteredpersonel',
            field=models.ForeignKey(null=True, verbose_name='Entered by', blank=True, to='iwmiproject.SystemUser'),
        ),
        migrations.AddField(
            model_name='seedmanagement',
            name='enteredpersonel',
            field=models.ForeignKey(null=True, verbose_name='Entered by', blank=True, to='iwmiproject.SystemUser'),
        ),
    ]
