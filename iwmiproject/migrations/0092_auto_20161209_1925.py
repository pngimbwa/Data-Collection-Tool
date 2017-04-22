# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0091_yieldrowbedlevel_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantingmethod',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', blank=True, to='iwmiproject.Farm', null=True),
        ),
        migrations.AddField(
            model_name='soilproperty',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', blank=True, to='iwmiproject.Farm', null=True),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', blank=True, to='iwmiproject.Farm', null=True),
        ),
    ]
