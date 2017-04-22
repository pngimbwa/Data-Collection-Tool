# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0003_people_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='group',
            field=models.ForeignKey(null=True, to='iwmi.Group', blank=True, verbose_name='Group'),
        ),
    ]
