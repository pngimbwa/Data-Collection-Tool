# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0043_auto_20161123_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='enteredpersonel',
            field=models.ForeignKey(verbose_name='Entered by', blank=True, to='iwmiproject.SystemUser', null=True),
        ),
    ]
