# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0021_transplanting_enteredpersonel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizermanagement',
            name='price_unit',
            field=models.CharField(null=True, verbose_name='Price Unit', max_length=10, blank=True),
        ),
    ]
