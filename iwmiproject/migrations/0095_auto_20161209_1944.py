# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0094_plotirrigationevent_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='residualhandling',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', verbose_name='Farm', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='weed',
            name='farm',
            field=models.ForeignKey(to='iwmiproject.Farm', verbose_name='Farm', null=True, blank=True),
        ),
    ]
