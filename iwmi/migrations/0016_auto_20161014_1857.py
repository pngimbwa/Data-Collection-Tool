# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0015_nursery_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nursery',
            name='crop',
        ),
        migrations.AddField(
            model_name='nursery',
            name='seed',
            field=models.ForeignKey(to='iwmi.Seed', default='none', verbose_name='seed'),
        ),
    ]
