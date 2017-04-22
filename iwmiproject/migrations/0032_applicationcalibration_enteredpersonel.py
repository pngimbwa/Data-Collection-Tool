# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0031_auto_20161113_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationcalibration',
            name='enteredpersonel',
            field=models.ForeignKey(null=True, blank=True, to='iwmiproject.SystemUser', verbose_name='Entered by'),
        ),
    ]
