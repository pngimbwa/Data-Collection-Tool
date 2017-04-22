# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0020_auto_20161107_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='transplanting',
            name='enteredpersonel',
            field=models.ForeignKey(blank=True, verbose_name='Entered by', null=True, to='iwmiproject.SystemUser'),
        ),
    ]
