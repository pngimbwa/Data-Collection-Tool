# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0086_remark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remark',
            options={'ordering': ['plot']},
        ),
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='dripline_length',
        ),
        migrations.RemoveField(
            model_name='plotirrigationevent',
            name='dripline_spacing',
        ),
        migrations.AlterField(
            model_name='plotirrigationevent',
            name='irrigated_depth',
            field=models.FloatField(blank=True, null=True, verbose_name='Irrigated depth(mm)'),
        ),
    ]
