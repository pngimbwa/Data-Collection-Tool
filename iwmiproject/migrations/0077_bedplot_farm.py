# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0076_plantingmethod_total_plants'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedplot',
            name='farm',
            field=models.ForeignKey(verbose_name='Farm', null=True, blank=True, to='iwmiproject.Farm'),
        ),
    ]
